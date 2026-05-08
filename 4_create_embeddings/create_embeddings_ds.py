"""Creates dataset.pt from bioBERT embeddings"""

import ast
import os
import sys
import torch
import pandas as pd

embedding_dir = "./final"
dir_name = os.path.basename(embedding_dir.rstrip("/"))
output_file = f"{dir_name}_dataset.pt"

df = pd.read_csv("./datasets/dataset_251.csv")

X, y = [], []

# load embeddings
def load_embedding_desc(drug_name):
    path = os.path.join("./drug_embeddings/SAMPLE_biobert_description_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_tox(drug_name):
    path = os.path.join("./drug_embeddings/SAMPLE_biobert_toxicity_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_smiles(drug_name):
    path = os.path.join("./drug_embeddings/SAMPLE_biobert_SMILES_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_pharmaco(drug_name):
    path = os.path.join("./drug_embeddings/SAMPLE_biobert_pharmacodynamics_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_halflife(drug_name):
    path = os.path.join("./drug_embeddings/SAMPLE_biobert_half-life_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

# process drug pairs
for _, row in df.iterrows():
    name = row['db_name']
    label = row['labels']
    label = ast.literal_eval(label)
    emb_description = load_embedding_desc(name)
    emb_tox= load_embedding_tox(name)
    emb_smiles = load_embedding_smiles(name)
    emb_pharmaco = load_embedding_pharmaco(name)
    emb_halflife = load_embedding_halflife(name)


    if emb_description is None or emb_tox is None or emb_smiles is None or emb_pharmaco is None or emb_halflife is None:
        continue

    X.append(emb_description)
    X.append(emb_tox)
    X.append(emb_smiles)
    X.append(emb_pharmaco)
    X.append(emb_halflife)
    y.append(label)
    
# convert to tensor
X = torch.stack(X)
y = torch.tensor(y)

# print summary
print(f"\n completed making dataset!")
print(f" - original number of index: {len(torch.unique(y))}")
print(f" - list of index: {torch.unique(y).tolist()}")

# save file
torch.save((X, y), output_file)
print(f"\n saved as: {output_file}")