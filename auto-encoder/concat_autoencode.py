from sentence_transformers import SentenceTransformer

import numpy as np
import torch
import sys

models = {
            "mxbai"     : "mixedbread-ai/mxbai-embed-large-v1",
            "bge"       : "BAAI/bge-large-en-v1.5"                 ,
            "e5"        : "intfloat/e5-large-v2"              ,
            "snowflake" : "Snowflake/snowflake-arctic-embed-m",
            "snowflake-l" : "Snowflake/snowflake-arctic-embed-l",
            "gte-base"        : "thenlper/gte-base",
            "gte-large"       : "thenlper/gte-large",
            "gte-small"       : "thenlper/gte-small"
}

nm1 = "e5"
nm2 = "mxbai"

model_names = [models[nm1], models[nm2]]
main_models = [SentenceTransformer(nm).to("cuda") for nm in model_names]

INPUT_DIM       = int(sys.argv[1])
COMPRESSED_DIM  = int(sys.argv[2])

CHECKPOINT_PATH = None 

if len(sys.argv) > 3:
    CHECKPOINT_PATH = sys.argv[3]

import torch.nn as nn

class AutoEncoder(nn.Module):
    def __init__(self, input_dim=INPUT_DIM, compressed_dim=COMPRESSED_DIM):
        super(AutoEncoder, self).__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 1024),
            nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(512, compressed_dim),
            nn.BatchNorm1d(compressed_dim),
            nn.LeakyReLU(0.2, inplace=True)
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(compressed_dim, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(512, 1024),
            nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, input_dim),
        )
        
    def forward(self, x):
        
        compressed = self.encoder(x)
        reconstructed = self.decoder(compressed)
        
        return reconstructed, compressed

class CombinedSentenceTransformer:
    def __init__(
        self, 
        models, 
        autoencoder_path: str = None,
        input_dim: int = 2048,  
        compressed_dim: int = 1024,
        device: str = "cuda"
    ):
        self.models = models
        self.device = device
        for model in self.models:
            model.to(self.device)
            model.eval()
        
        if autoencoder_path:
            print(autoencoder_path)
            self.use_autoencoder = True
            self.autoencoder = AutoEncoder(input_dim=input_dim, compressed_dim=compressed_dim)
            self.autoencoder.load_state_dict(torch.load(autoencoder_path, map_location=self.device))
            self.autoencoder.to(self.device)
            self.autoencoder.eval()  # Set to evaluation mode
        else:
            self.use_autoencoder = False
            self.autoencoder = None

    def encode(
        self,
        sentences,
        batch_size=32,
        show_progress_bar=False,
        device="cuda",
        convert_to_numpy=True,
        convert_to_tensor=False,
        normalize_embeddings=False,
        use_autoencoder: bool = None,
        **kwargs  # Capture all additional keyword arguments
    ):
        """
        Encode sentences by concatenating embeddings from all models.

        Parameters:
        - sentences (List[str]): List of sentences to encode. # I take pre-embedded sentences.
        - **kwargs: Additional keyword arguments. # this prevenets some errors, thanks o1

        Returns:
        - Combined embeddings as NumPy array or PyTorch tensor.
        """
        if device:
            self.to(device)

        # Filter out unexpected keyword arguments
        # Define allowed kwargs based on SentenceTransformer.encode's signature
        allowed_kwargs = {
            'convert_to_numpy',
            'convert_to_tensor',
            'normalize_embeddings',
            'output_value',  
			# Added based on SentenceTransformer.encode
            # Add other allowed kwargs if necessary
        }

        # Extract only allowed kwargs
        # Optionally, log or handle unexpected kwargs
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in allowed_kwargs}
        unexpected_kwargs = set(kwargs.keys()) - allowed_kwargs
        if unexpected_kwargs:
            print(f"Warning: Ignoring unexpected keyword arguments: {unexpected_kwargs}")

        # Encode with each model
        
        ## should be an if-else here on model lenghts. is it only one model or 2 or ...
        embeddings = [
            model.encode(
                sentences,
                batch_size=batch_size,
                show_progress_bar=show_progress_bar,
                device=device,
                convert_to_numpy=True,  # Always get NumPy for concatenation
                normalize_embeddings=normalize_embeddings,
                **filtered_kwargs  # Pass only allowed kwargs
            )
            for model in self.models
        ]

        combined_embeddings = np.concatenate(embeddings, axis=1)
        combined_tensor = torch.tensor(combined_embeddings, dtype=torch.float32).to(device)

        apply_autoencoder = use_autoencoder if use_autoencoder is not None else self.use_autoencoder
        if apply_autoencoder and self.autoencoder:
            with torch.no_grad():
                compressed_embeddings = self.autoencoder.encoder(combined_tensor)
            embeddings_to_return = compressed_embeddings
        else:
            embeddings_to_return = combined_tensor 

        # Convert to desired format
        if convert_to_numpy:
            embeddings_to_return = embeddings_to_return.cpu().numpy()
        elif convert_to_tensor:
            embeddings_to_return = embeddings_to_return
        else:
            embeddings_to_return = embeddings_to_return

        return embeddings_to_return

    def to(self, device):
        self.device = device
        for model in self.models:
            model.to(device)
        if self.use_autoencoder and self.autoencoder:
            self.autoencoder.to(device)

autoencoder_path_ = None
if CHECKPOINT_PATH is not None:
    autoencoder_path_ = f'models_pth/{INPUT_DIM}_{COMPRESSED_DIM}/{CHECKPOINT_PATH}'

combined_model = CombinedSentenceTransformer(
    models=main_models,
    autoencoder_path=autoencoder_path_,  
    input_dim= INPUT_DIM,  
    compressed_dim= COMPRESSED_DIM,
    device='cuda' if torch.cuda.is_available() else 'cpu'
)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
combined_model.to(device)

sentence = ["convert_to_numpy (bool): Whether to convert embeddings to NumPy arrays."]



eval_ = True 
if eval_:
    import mteb
    tasks = mteb.get_tasks(tasks=["NFCorpus"]) 
    evaluation = mteb.MTEB(tasks=tasks, eval_splits=["test"], metric="ndcg@10")
    results = evaluation.run(combined_model, output_folder = f"results/mix01_{COMPRESSED_DIM}_{CHECKPOINT_PATH}")



