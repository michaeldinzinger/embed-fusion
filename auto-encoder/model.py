# model.py

import torch.nn as nn
from config import INPUT_DIM, COMPRESSED_DIM


n_0 = 1792 
n_1 = 1280
n_2 = 1024

class AutoEncoder(nn.Module):
    def __init__(self, input_dim=1, compressed_dim=1):
        super(AutoEncoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, n_0),
            nn.BatchNorm1d(n_0),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(n_0, n_1),
            nn.BatchNorm1d(n_1),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(n_1, compressed_dim),
        )

        # Decoder
        self.decoder = nn.Sequential(

            nn.Linear(compressed_dim, n_1),
            nn.BatchNorm1d(n_1),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(n_1, n_0),
            nn.BatchNorm1d(n_0),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(n_0, input_dim),
        )

    def forward(self, x):
        compressed = self.encoder(x)
        reconstructed = self.decoder(compressed)
        return reconstructed, compressed

def initialize_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        if m.bias is not None:
            nn.init.zeros_(m.bias)

"""
class AutoEncoder(nn.Module):
    def __init__(self, input_dim=INPUT_DIM, compressed_dim=COMPRESSED_DIM):
        super(AutoEncoder, self).__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 1500),
            nn.BatchNorm1d(1500),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1500, 1024),
            nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            #nn.Linear(1024, 512),
            #nn.BatchNorm1d(512),
            #nn.LeakyReLU(0.2, inplace=True),

            #nn.Linear(1024, 512),
            #nn.BatchNorm1d(512),
            #nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, 768),
            nn.BatchNorm1d(compressed_dim),
            nn.LeakyReLU(0.2, inplace=True)
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(compressed_dim, 1024),
            nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, 1500),
            nn.BatchNorm1d(1500),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1500, input_dim),
        )
        
    def forward(self, x):
        compressed = self.encoder(x)
        reconstructed = self.decoder(compressed)
        
        return reconstructed, compressed

def initialize_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        if m.bias is not None:
            nn.init.zeros_(m.bias)
	
"""