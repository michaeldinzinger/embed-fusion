import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import numpy as np
from tqdm import tqdm
import re
from sklearn.model_selection import train_test_split

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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

all_paragraphs = all_paragraphs[:500_000]


num_samples = len(all_paragraphs)
print(f"Total passages collected: {num_samples}")

train_indices, val_indices = train_test_split(
    np.arange(num_samples),
    test_size=0.2,  # 80% train, 20% validation
    random_state=42,
    shuffle=True
)

print(f"Train set size: {len(train_indices)}")
print(f"Validation set size: {len(val_indices)}")

# Save the split indices
save_dir = "embeddings_data/split_indices"
os.makedirs(save_dir, exist_ok=True)

np.save(os.path.join(save_dir, "train_indices.npy"), train_indices)
np.save(os.path.join(save_dir, "val_indices.npy"), val_indices)
print(f"Train and validation indices saved to: {save_dir}")

import pickle
passages_save_path = os.path.join(save_dir, "all_paragraphs.pkl")
with open(passages_save_path, 'wb') as f:
    pickle.dump(all_paragraphs, f)
print(f"All paragraphs saved to: {passages_save_path}")
