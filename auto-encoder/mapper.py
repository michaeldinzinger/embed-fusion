import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the data
path_1 = "../data/mix_train_embeddings.npy"
path_2 = "../data/bge-small_wiki_500k/train_embeddings.npy"
path_3 = "../data/e5-small_wiki_500k/train_embeddings.npy"

data_2 = np.load(path_2)
data_3 = np.load(path_3)

input_data  = np.concatenate((data_2, data_3), axis=1)
target_data = np.load(path_1)

# Normalize the data

scaler_input = StandardScaler()
input_data = scaler_input.fit_transform(input_data)

scaler_target = StandardScaler()
target_data = scaler_target.fit_transform(target_data)

# Convert to tensors

input_tensor = torch.from_numpy(input_data).float()
target_tensor = torch.from_numpy(target_data).float()

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    input_tensor, target_tensor, test_size=0.1, random_state=42
)

# Create DataLoaders
batch_size = 256

train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataset = TensorDataset(X_val, y_val)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Define the model
class MappingNet(nn.Module):
    def __init__(self):
        super(MappingNet, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(768, 1024),
            nn.ReLU(),
            nn.Dropout(p=0.3),

            nn.Linear(1024, 1024),
            nn.ReLU(),
            nn.Dropout(p=0.3),

            nn.Linear(1024, 1024),
            nn.ReLU(),
            nn.Dropout(p=0.3),

            nn.Linear(1024, 768)
        )

    def _initialize_weights(self):
        for m in self.layers:
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                nn.init.zeros_(m.bias)

    def forward(self, x):
        return self.layers(x)

# Initialize the model
model = MappingNet()
model._initialize_weights()

# Check for GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

# Training loop with validation
num_epochs = 30
best_val_loss = float('inf')
patience = 5
trigger_times = 0

for epoch in range(num_epochs):
    # Training
    model.train()
    total_train_loss = 0
    for batch_inputs, batch_targets in train_loader:
        batch_inputs = batch_inputs.to(device)
        batch_targets = batch_targets.to(device)

        optimizer.zero_grad()
        outputs = model(batch_inputs)
        loss = criterion(outputs, batch_targets)
        loss.backward()
        optimizer.step()

        total_train_loss += loss.item()

    avg_train_loss = total_train_loss / len(train_loader)

    # Validation
    model.eval()
    total_val_loss = 0
    with torch.no_grad():
        for batch_inputs, batch_targets in val_loader:
            batch_inputs = batch_inputs.to(device)
            batch_targets = batch_targets.to(device)

            outputs = model(batch_inputs)
            loss = criterion(outputs, batch_targets)
            total_val_loss += loss.item()

    avg_val_loss = total_val_loss / len(val_loader)

    print(f"Epoch [{epoch+1}/{num_epochs}], "
          f"Train Loss: {avg_train_loss:.6f}, "
          f"Val Loss: {avg_val_loss:.6f}")

    # Early stopping
    if avg_val_loss < best_val_loss:
        best_val_loss = avg_val_loss
        trigger_times = 0
        # Save the best model
        torch.save(model.state_dict(), 'best_model_jj.pth')
    else:
        trigger_times += 1
        if trigger_times >= patience:
            print("Early stopping triggered.")
            break

print("Training completed.")
