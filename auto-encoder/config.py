
# config.py

import os
import torch

# Device configuration
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

SAVE_DIR = "embeddings_data/e5_embed_wiki"

TRAIN_SAVE_PATH = os.path.join(SAVE_DIR, "train_embeddings.npz")
VAL_SAVE_PATH = os.path.join(SAVE_DIR, "val_embeddings.npz")


RECONSTRUCTIONS_DIR = "reconstructions"

BATCH_SIZE = 64
NUM_EPOCHS = 100

# optimizer
LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-5

# scheduler
STEP_SIZE = 20
GAMMA = 0.1

PATIENCE = 10

# autoenc
INPUT_DIM = 1024 
COMPRESSED_DIM = 900 

BEST_MODEL_PATH = f"best_encoder_e5_{COMPRESSED_DIM}.pth"

# can we optimmize this? why 64 work worse? where do you even need it?
NUM_WORKERS = 64 


# why not this? 
TOKENIZERS_PARALLELISM = "false"