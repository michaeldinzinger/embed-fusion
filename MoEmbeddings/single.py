import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.manifold import TSNE

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


path_to_data = "../data" 

train_e5_small_path            = f"{path_to_data}/e5-small_wiki_500k/train_embeddings.npy"
val_e5_small_path              = f"{path_to_data}/e5-small_wiki_500k/val_embeddings.npy"

train_e5_large_autoencode_path = f"{path_to_data}/e5_wiki_500k/train_embeddings.npy"
val_e5_large_autoencode_path   = f"{path_to_data}/e5_wiki_500k/val_embeddings.npy"

# Load data
train_e5_small = np.load(train_e5_small_path)           # Shape: (num_train_samples, 384)
train_e5_large_autoencode = np.load(train_e5_large_autoencode_path)  # Shape: (num_train_samples, 384)
val_e5_small = np.load(val_e5_small_path)               # Shape: (num_val_samples, 384)
val_e5_large_autoencode = np.load(val_e5_large_autoencode_path)      # Shape: (num_val_samples, 384)

# Convert NumPy arrays to PyTorch tensors
X_train_tensor = torch.tensor(train_e5_small, dtype=torch.float32)
y_train_tensor = torch.tensor(train_e5_large_autoencode, dtype=torch.float32)
X_val_tensor   = torch.tensor(val_e5_small, dtype=torch.float32)
y_val_tensor   = torch.tensor(val_e5_large_autoencode, dtype=torch.float32)


# Define batch size
batch_size = 34

# Create TensorDatasets
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
val_dataset   = TensorDataset(X_val_tensor, y_val_tensor)

# Create DataLoaders
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader   = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# model
class EmbedMappingNN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(EmbedMappingNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Linear(input_dim, 384),
            nn.BatchNorm1d(384),
            nn.ELU(),
            nn.Dropout(0.3)
        )
        self.layer2 = nn.Sequential(
            nn.Linear(384, 512),
            nn.BatchNorm1d(512),
            nn.ELU(),
            nn.Dropout(0.3)
        )

        self.layer3 = nn.Sequential(
            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ELU(),
            nn.Dropout(0.3)
        )
        self.output_layer = nn.Linear(512, output_dim)
        self.initialize_weights()
    
    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out) 
        out = self.layer3(out) + out  # Residual connection
        out = self.output_layer(out)
        return out

    def initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, nn.BatchNorm1d):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)



class RegularizedCombinedLoss(nn.Module):
    def __init__(self, mse_weight=0.9, cosine_weight=0.1, l2_weight=1e-5):
        super(RegularizedCombinedLoss, self).__init__()
        self.mse = nn.MSELoss()
        self.cosine = nn.CosineEmbeddingLoss()
        self.mse_weight = mse_weight
        self.cosine_weight = cosine_weight
        self.l2_weight = l2_weight

    def forward(self, output, target, model):
        loss_mse = self.mse(output, target)
        labels = torch.ones(output.size(0)).to(output.device)
        loss_cosine = self.cosine(output, target, labels)
        
        l2_reg = torch.tensor(0.).to(output.device)
        for param in model.parameters():
            l2_reg += torch.norm(param)
        
        loss = (
            self.mse_weight * loss_mse +
            self.cosine_weight * loss_cosine +
            self.l2_weight * l2_reg
        )
        return loss

if __name__ == "__main__":
    model = EmbedMappingNN(384, 1024)

    criterion = RegularizedCombinedLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-2)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=4, gamma=0.1)
    #scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=5, factor=0.5) 

    num_epochs = 15
    best_val_loss = float('inf')

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for batch_X, batch_y in train_loader:
            #print(batch_X.shape, batch_y.shape)
            optimizer.zero_grad()
            outputs = model(batch_X)
            #loss = criterion(outputs, batch_y)
            loss = criterion(outputs, batch_y, model)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * batch_X.size(0)
        
        epoch_train_loss = running_loss / len(train_loader.dataset)
        
        # Validation Phase
        model.eval()
        val_running_loss = 0.0
        with torch.no_grad():
            for batch_X, batch_y in val_loader:
                outputs = model(batch_X)
                loss = criterion(outputs, batch_y, model)
                val_running_loss += loss.item() * batch_X.size(0)
        epoch_val_loss = val_running_loss / len(val_loader.dataset)
        
        print(f'Epoch {epoch+1}/{num_epochs}, Training Loss: {epoch_train_loss:.6f}, Validation Loss: {epoch_val_loss:.6f}')
        
        # Step the scheduler
        scheduler.step(epoch_val_loss)
        
        # Save the best model
        if epoch_val_loss < best_val_loss:
            best_val_loss = epoch_val_loss
            torch.save(model.state_dict(), 'best_embed_mapping_model.pth')
            print("Best model saved.")

## eval

"""
model.load_state_dict(torch.load('best_embed_mapping_model.pth'))
model.eval()

with torch.no_grad():
    mapped_embeddings = model(X_val_tensor).numpy()

mse = mean_squared_error(val_e5_large_autoencode_normalized, mapped_embeddings)
cos_sim = cosine_similarity(val_e5_large_autoencode_normalized, mapped_embeddings).mean()

print(f'Validation MSE: {mse:.6f}')
print(f'Average Cosine Similarity: {cos_sim:.4f}')

# 9. Visualization
subset_size = 1000
y_val_subset = val_e5_large_autoencode_normalized[:subset_size]
mapped_subset = mapped_embeddings[:subset_size]

tsne = TSNE(n_components=2, random_state=42)
y_val_2d = tsne.fit_transform(y_val_subset)
mapped_2d = tsne.fit_transform(mapped_subset)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(y_val_2d[:, 0], y_val_2d[:, 1], alpha=0.5)
plt.title('Original e5-large-autoencode Embeddings')

plt.subplot(1, 2, 2)
plt.scatter(mapped_2d[:, 0], mapped_2d[:, 1], alpha=0.5, color='orange')
plt.title('Mapped e5-small Embeddings')

plt.show()

## things to try, combine mseloss with cosime-sim

class CombinedLoss(nn.Module):
    def __init__(self, mse_weight=1.0, cosine_weight=1.0):
        super(CombinedLoss, self).__init__()
        self.mse = nn.MSELoss()
        self.cosine = nn.CosineSimilarity(dim=1)
        self.mse_weight = mse_weight
        self.cosine_weight = cosine_weight

    def forward(self, output, target):
        loss_mse = self.mse(output, target)
        loss_cosine = 1 - self.cosine(output, target).mean()
        return self.mse_weight * loss_mse + self.cosine_weight * loss_cosine

# Use CombinedLoss instead of MSELoss
criterion = CombinedLoss(mse_weight=1.0, cosine_weight=1.0)

"""