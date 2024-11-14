import click
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from ef.utils import *


class SparseAutoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim, l1_penalty=1e-5):
        super(SparseAutoencoder, self).__init__()
        
        # Encoder
        self.encoder = nn.Linear(input_dim, latent_dim)
        # Decoder
        self.decoder = nn.Linear(latent_dim, input_dim)
        
        # Sparsity regularization
        self.l1_penalty = l1_penalty

    def forward(self, x):
        # Apply encoder
        encoded = torch.relu(self.encoder(x))
        # Apply decoder
        decoded = torch.sigmoid(self.decoder(encoded))
        return encoded, decoded
    
    def get_l1_loss(self):
        l1_loss = 0
        for param in self.parameters():
            l1_loss += torch.sum(torch.abs(param))
        return self.l1_penalty * l1_loss


def train_autoencoder(dense_vectors, latent_dim=10000, l1_penalty=1e-5, 
                      learning_rate=0.001, epochs=50, batch_size=128, validation_split=0.2):
    
    input_dim = dense_vectors.shape[1]  # Dimension of the dense embeddings
    
    # Convert numpy data to PyTorch tensors
    dense_vectors_tensor = torch.tensor(dense_vectors, dtype=torch.float32)

    # Create dataset and dataloaders
    dataset = TensorDataset(dense_vectors_tensor, dense_vectors_tensor)  # Input and target are the same
    train_size = int((1 - validation_split) * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    # Initialize model, loss function, and optimizer
    model = SparseAutoencoder(input_dim, latent_dim, l1_penalty=l1_penalty)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training loop
    for epoch in range(epochs):
        model.train()
        train_loss = 0
        for batch in train_loader:
            inputs, targets = batch
            
            # Forward pass
            _, decoded = model(inputs)
            
            # Compute loss (reconstruction loss + L1 regularization)
            loss = criterion(decoded, targets) + model.get_l1_loss()
            
            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # Validation
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for batch in val_loader:
                inputs, targets = batch
                _, decoded = model(inputs)
                loss = criterion(decoded, targets)
                val_loss += loss.item()
        
        click.echo(f"Epoch {epoch + 1}/{epochs}, Train Loss: {train_loss/len(train_loader)}, Val Loss: {val_loss/len(val_loader)}")
    
    return model


@click.command()
@click.argument("method", type=click.Choice(['train', 'evaluate']))
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
def sae(method: str, pretrained_model_name: str):
    """
    Train and infer a Sparse Autoencoder.
    """
    click.echo(f"Method: {method}")
    click.echo(f"Pretrained model name: {pretrained_model_name}")

    # Hyperparameters
    latent_dim = 10_000      # Dimensionality of the sparse latent space
    l1_penalty = 1e-5        # L1 regularization strength
    learning_rate = 0.001    # Learning rate
    epochs = 10              # Number of training epochs
    batch_size = 128         # Batch size

    # Model path
    model_path = os.path.join(RESULTS_FOLDER, 'sae', pretrained_model_name.replace("/", "_"), 'model.pt')
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    # Embeddings path
    embeddings_path = os.path.join(RESULTS_FOLDER, 'embeddings', pretrained_model_name.replace("/", "_"))

    if method == 'train':
        # Load corpus embeddings for passages
        path = os.path.join(embeddings_path, f'id_100_mid.jsonl')
        if not os.path.exists(path):
            raise ValueError(f'No corpus embeddings found for pretrained model {pretrained_model_name}')
        df_corpus = pd.read_json(path, orient='records', lines=True).set_index('corpus-id')
        dense_vectors = np.array(df_corpus['embedding'].to_list())

        # Train the autoencoder
        autoencoder = train_autoencoder(
            dense_vectors=dense_vectors,
            latent_dim=latent_dim, 
            l1_penalty=l1_penalty, 
            learning_rate=learning_rate, 
            epochs=epochs,
            batch_size=batch_size
        )

        # Save the encoder model
        torch.save(autoencoder, model_path)

    elif method == 'evaluate':
        # Load the encoder model
        autoencoder = torch.load(model_path, weights_only=False)

        # Load corpus embeddings for passages
        path = os.path.join(embeddings_path, f'id_100_mid.jsonl')
        if not os.path.exists(path):
            raise ValueError(f'No corpus embeddings found for pretrained model {pretrained_model_name}')
        df_corpus = pd.read_json(path, orient='records', lines=True).set_index('corpus-id')
        dense_vectors = np.array(df_corpus['embedding'].to_list()[-1_000:])

        # Generate sparse vectors from your dense embeddings
        dense_vectors_tensor = torch.tensor(dense_vectors, dtype=torch.float32)
        with torch.no_grad():
            sparse_vectors, _ = autoencoder(dense_vectors_tensor)

        # Save sparse vectors or use them for retrieval
        click.echo(sparse_vectors.shape)

    else:
        click.echo('Invalid method. Choose between "train" and "evaluate".')
