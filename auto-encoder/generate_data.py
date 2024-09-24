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

# Load E5
e5_model_name = 'intfloat/e5-large-v2'
e5_tokenizer = AutoTokenizer.from_pretrained(e5_model_name)
e5_model = AutoModel.from_pretrained(e5_model_name).to(device)
e5_model.eval()

# Load MXBAI
mxbai_model_name = 'mixedbread-ai/mxbai-embed-large-v1'
mxbai_tokenizer = AutoTokenizer.from_pretrained(mxbai_model_name)
mxbai_model = AutoModel.from_pretrained(mxbai_model_name).to(device)
mxbai_model.eval()

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

# Create Dataset and DataLoader

paragraph_dataset = ParagraphDataset(all_paragraphs[:10000]) 
batch_size = 64
data_loader = DataLoader(paragraph_dataset, batch_size=batch_size, shuffle=False, num_workers = 96)

import torch.nn.functional as F
from torch import Tensor

def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

from typing import Dict
def pooling(outputs: torch.Tensor, inputs: Dict,  strategy: str = 'cls') -> np.ndarray:
    if strategy == 'cls':
        outputs = outputs[:, 0]
    elif strategy == 'mean':
        outputs = torch.sum(
            outputs * inputs["attention_mask"][:, :, None], dim=1) / torch.sum(inputs["attention_mask"], dim=1, keepdim=True)
    else:
        raise NotImplementedError
    return outputs.detach().cpu().numpy()


def generate_e5_embeddings_batch(data_loader, model, tokenizer, device, max_length=512):
    embeddings = []
    model.eval()

    for texts in tqdm(data_loader, desc="Generating E5 Embeddings in Batches"):
        # Tokenize the batch of texts
        inputs = tokenizer(
            texts,
            return_tensors='pt',
            truncation=True,
            padding='max_length',
            max_length=max_length
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            last_hidden_states = outputs.last_hidden_state
            attention_mask = inputs['attention_mask']
            pooled_output = average_pool(last_hidden_states, attention_mask)
            pooled_output = F.normalize(pooled_output, p=2, dim=1)

            embeddings.append(pooled_output.cpu().numpy())

    return np.vstack(embeddings)

def generate_mxbai_embeddings_batch(data_loader, model, tokenizer, device, max_length=512, strategy='cls'):
    embeddings = []
    model.eval()

    for texts in tqdm(data_loader, desc="Generating MXBAI Embeddings in Batches"):
        # Tokenize the batch of texts
        inputs = tokenizer(
            texts,
            return_tensors='pt',
            truncation=True,
            padding='max_length',
            max_length=max_length
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            last_hidden_states = outputs.last_hidden_state
            pooled_output = pooling(last_hidden_states, inputs, strategy=strategy)
            embeddings.append(pooled_output)

    return np.vstack(embeddings)



e5_embeddings = generate_e5_embeddings_batch(data_loader, e5_model, e5_tokenizer, device, max_length=128)
mxbai_embeddings = generate_mxbai_embeddings_batch(data_loader, mxbai_model, mxbai_tokenizer, device, max_length=128)
concatenated_embeddings = np.hstack((e5_embeddings, mxbai_embeddings)) 

save_dir = "embeddings_data"

os.makedirs(save_dir, exist_ok=True)

#train_data, val_data = train_test_split(concatenated_embeddings, test_size=0.2, random_state=42)
#train_save_path = os.path.join(save_dir, "train_embeddings.npz")

#val_save_path = os.path.join(save_dir, "val_embeddings.npz")

#np.savez(train_save_path, embeddings=train_data)
#np.savez(val_save_path, embeddings=val_data)

#print(f"Train embeddings saved to: {train_save_path}")
#print(f"Validation embeddings saved to: {val_save_path}")


