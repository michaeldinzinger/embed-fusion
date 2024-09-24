import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

import numpy as np
import pandas as pd

from transformers import AutoTokenizer, AutoModel
from datasets import load_dataset, Dataset as HFDataset

from tqdm import tqdm
import re
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 2. Load Models and Tokenizers
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


model_name = 'intfloat/e5-large-v2'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name).to(device)
model.eval()

# Prepare Dataset, pre-process it
wikipedia = load_dataset('wikipedia', '20220301.en', split='train[:1%]')  # Adjust slice as needed

def split_into_paragraphs(text):
    paragraphs = re.split(r'\n{2,}', text)
    paragraphs = [para.strip().replace('\n', ' ') for para in paragraphs if para.strip()]
    return paragraphs

all_paragraphs = []
for article in tqdm(wikipedia, desc="Processing Articles"):
    text = article['text']
    paragraphs = split_into_paragraphs(text)
    filtered_paras = [para for para in paragraphs if len(para.split()) >= 50]
    all_paragraphs.extend(filtered_paras)



class ParagraphDataset(Dataset):
    def __init__(self, paragraphs):
        self.paragraphs = paragraphs
    
    def __len__(self):
        return len(self.paragraphs)
    
    def __getitem__(self, idx):
        return self.paragraphs[idx]


paragraph_dataset = ParagraphDataset(all_paragraphs[:200_000]) 

batch_size = 64
data_loader = DataLoader(paragraph_dataset, batch_size=batch_size, shuffle=False, num_workers = 96)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('intfloat/e5-large-v2').to(device)
embeddings = []
#model.eval()
for texts in tqdm(data_loader, desc="Generating Embeddings Batches"):
    emb = model.encode(texts, normalize_embeddings=True)
    embeddings.append(emb)

embeddings = np.vstack(embeddings)

#embeddings = generate_embeddings(data_loader, model)

save_dir = "embeddings_data/e5_embed_wiki"
os.makedirs(save_dir, exist_ok=True)

"""
#dimensions = 512
model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
embeddings = []
#model.eval()
for texts in tqdm(data_loader, desc="Generating Embeddings Batches"):
    emb = model.encode(texts)
    embeddings.append(emb)

embeddings = np.vstack(embeddings)
print(embeddigns.shape)
"""

save_dir = "embeddings_data/e5_embed_wiki"


train_data, val_data = train_test_split(embeddings, test_size=0.2, random_state=42)

train_save_path = os.path.join(save_dir, "train_embeddings.npz")
val_save_path = os.path.join(save_dir, "val_embeddings.npz")

np.savez(train_save_path, embeddings=train_data)
np.savez(val_save_path, embeddings=val_data)

print(f"Train embeddings saved to: {train_save_path}")
print(f"Validation embeddings saved to: {val_save_path}")


