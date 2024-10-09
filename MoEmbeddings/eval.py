from sentence_transformers import SentenceTransformer
import mteb 

import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
#from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

from typing import List, Union
from single import EmbedMappingNN

INPUT_DIM      = 384
COMPRESSED_DIM = 1024 
OUTPUT_DIM     = 1024 
#model_path = "best_embed_mapping_model.pth" 
#model_path = f'models_pth/{INPUT_DIM}_{COMPRESSED_DIM}/{CHECKPOINT_PATH}'

print("wtf?")

class EmbedEncode:
    def __init__(
        self, 
        model: SentenceTransformer, 
        mapping_model_path: str = None,
        input_dim: int = 384,  # e5-small embedding size
        output_dim: int = 384, # e5-large-autoencode output size
        device: str = "cuda"
    ):

        self.model = model
        self.device = device
        self.model.to(self.device)
        self.model.eval()
        
        if mapping_model_path:
            self.use_mapping = True
            self.mapping_model = EmbedMappingNN(input_dim=INPUT_DIM, output_dim=OUTPUT_DIM)
            self.mapping_model.load_state_dict(torch.load(mapping_model_path, map_location=self.device))
            self.mapping_model.to(self.device)
            self.mapping_model.eval()  # Set to evaluation mode
        else:
            self.use_mapping = False
            self.mapping_model = None

    def encode(
        self,
        sentences: List[str],
        batch_size: int = 32,
        show_progress_bar: bool = False,
        device: str = None,
        convert_to_numpy: bool = True,
        convert_to_tensor: bool = False,
        normalize_embeddings: bool = False,
        use_mapping: bool = None,
        **kwargs
    ) -> Union[np.ndarray, torch.Tensor]:
        
        if device:
            self.to(device)

        allowed_kwargs = {
            'convert_to_numpy',
            'convert_to_tensor',
            'normalize_embeddings',
            'output_value',  
            # Add other allowed kwargs if necessary
        }

        # Extract only allowed kwargs
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in allowed_kwargs}

        # Optionally, log or handle unexpected kwargs
        unexpected_kwargs = set(kwargs.keys()) - allowed_kwargs
        if unexpected_kwargs:
            print(f"Warning: Ignoring unexpected keyword arguments: {unexpected_kwargs}")

        
        current_device = device if device else self.device

        # Encode sentences using the SentenceTransformer model
        embeddings = self.model.encode(
            sentences, 
            batch_size=batch_size, 
            show_progress_bar=show_progress_bar,
            device=current_device,
            convert_to_numpy  =False,  
            convert_to_tensor =True,  
            normalize_embeddings=normalize_embeddings,
            **filtered_kwargs  
        )
        
        # Ensure embeddings are on the correct device
        if not isinstance(embeddings, torch.Tensor):
            embeddings = torch.tensor(embeddings, dtype=torch.float32).to(current_device)
        else:
            embeddings = embeddings.to(current_device)

        # Determine whether to apply the mapping model
        apply_mapping = use_mapping if use_mapping is not None else self.use_mapping
        if apply_mapping and self.mapping_model:
            with torch.no_grad():
                mapped_embeddings = self.mapping_model(embeddings)
            embeddings_to_return = mapped_embeddings
        else:
            embeddings_to_return = embeddings

        # Convert to desired format
        if convert_to_numpy:
            embeddings_to_return = embeddings_to_return.cpu().numpy()
        elif convert_to_tensor:
            embeddings_to_return = embeddings_to_return
        else:
            embeddings_to_return = embeddings_to_return

        return embeddings_to_return

    def to(self, device: str):
        self.device = device
        self.model.to(device)
        if self.use_mapping and self.mapping_model:
            self.mapping_model.to(device)
 
models = {
            "mxbai"     : "mixedbread-ai/mxbai-embed-large-v1",  
            "bge"       : "BAAI/bge-large-en-v1.5"                 ,
            "e5"        : "intfloat/e5-large-v2"              ,
            "snowflake-m" : "Snowflake/snowflake-arctic-embed-m",
            "snowflake-l" : "Snowflake/snowflake-arctic-embed-l",
            "gte-base"        : "thenlper/gte-base",
            "gte-large"       : "thenlper/gte-large",
            "gte-small"       : "thenlper/gte-small",
            "e5-small"        : "intfloat/e5-small-v2", # (33M)
            "bge-small"       : "BAAI/bge-small-en-v1.5" # (33M)
}


print("wtf?")
 
model = SentenceTransformer(models["e5-small"]).to("cuda")

print("wtf?")

model_path = "best_embed_mapping_model.pth" 
# Initialize the EmbedEncode instance with the MappingModel
combined_model = EmbedEncode(
    model=model,
    mapping_model_path=model_path,  # Updated parameter name
    input_dim=INPUT_DIM,  
    output_dim=COMPRESSED_DIM,
    device='cuda' if torch.cuda.is_available() else 'cpu'
)

# Evaluation flag
r = np.random.randint(100)
r = 7
print(f"lucky numbe is {7}")
eval_ = True 
if eval_:
    tasks = mteb.get_tasks(tasks=["NFCorpus"]) 
    evaluation = mteb.MTEB(tasks=tasks, eval_splits=["test"], metric="ndcg@10")
    #results = evaluation.run(combined_model, output_folder = f"results/e5_{COMPRESSED_DIM}_{CHECKPOINT_PATH}") 
    results = evaluation.run(combined_model, output_folder = f"results/blabla_{r}") 