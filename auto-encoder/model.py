# model.py

import torch.nn as nn
from config import INPUT_DIM, COMPRESSED_DIM

class AutoEncoder(nn.Module):
    def __init__(self, input_dim=INPUT_DIM, compressed_dim=COMPRESSED_DIM):
        super(AutoEncoder, self).__init__()
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 1024),
            #nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, 512),
            #nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(512, compressed_dim),
            #nn.BatchNorm1d(compressed_dim),
            #nn.LeakyReLU(0.2, inplace=True)
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(compressed_dim, 512),
            #nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(512, 1024),
            #nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, input_dim),
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
	
