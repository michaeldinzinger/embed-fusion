import os
import sys
import sys
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

import numpy as np
import pandas as pd

#from transformers import AutoTokenizer, AutoModel
#from datasets import load_dataset, Dataset as HFDataset
#import re
#import matplotlib.pyplot as plt

from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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
            "bge-small"       : "BAAI/bge-small-en-v1.5", # (33M)
            "jina-v3"         : "jinaai/jina-embeddings-v3"
}

m_name = sys.argv[1]

split_dir = "split_indices"
wiki_path = os.path.join(split_dir, "all_paragraphs.pkl")

train_indices = np.load(os.path.join(split_dir, "train_indices.npy"))
val_indices   = np.load(os.path.join(split_dir, "val_indices.npy"))

import pickle
with open(wiki_path, 'rb') as f:
    all_paragraphs = pickle.load(f)

#all_paragraphs = all_paragraphs[:10_000] 

num_samples = len(all_paragraphs)
print(f"Train set size: {len(train_indices)}")
print(f"Validation set size: {len(val_indices)}")
print(f"Total passages loaded: {num_samples}")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = SentenceTransformer(models[m_name],
                            trust_remote_code = True
                            )
model.eval()

embeddings = []

batch_size = 32
num_batches = (len(all_paragraphs) + batch_size - 1) // batch_size

for i in tqdm(range(num_batches), desc="Generating Embeddings"):
    start_idx = i * batch_size
    end_idx = min((i + 1) * batch_size, len(all_paragraphs))
    batch_texts = all_paragraphs[start_idx:end_idx]

    batch_embeddings = model.encode(
        batch_texts,
        batch_size=batch_size,
        show_progress_bar=False,
        normalize_embeddings=True,
        convert_to_numpy=True,
        device=device
    )

    embeddings.append(batch_embeddings)

embeddings = np.vstack(embeddings)

print(f"Embeddings shape: {embeddings.shape}")


# Split embeddings based on saved indices
train_data = embeddings[train_indices]
val_data = embeddings[val_indices]

# Save embeddings using compressed .npz format to save space
save_dir = f"embeddings_data/{m_name}_wiki_500k"
os.makedirs(save_dir, exist_ok=True)

np.save(os.path.join(save_dir, "train_embeddings.npy"), train_data)
np.save(os.path.join(save_dir, "val_embeddings.npy"),   val_data)

print(f"Train embeddings saved to: {save_dir}/train_embeddings.npy")
print(f"Validation embeddings saved to: {save_dir}/val_embeddings.npy")


"""
class ParagraphDataset(Dataset):
    def __init__(self, paragraphs):
        self.paragraphs = paragraphs
    
    def __len__(self):
        return len(self.paragraphs)
    
    def __getitem__(self, idx):
        return self.paragraphs[idx]

paragraph_dataset = ParagraphDataset(all_paragraphs[:1000])
batch_size = 64
data_loader = DataLoader(paragraph_dataset, batch_size=batch_size, shuffle=False, num_workers=96)

"""
