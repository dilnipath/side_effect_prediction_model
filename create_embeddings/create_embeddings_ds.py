import ast
import os
import sys
import torch
import pandas as pd

# # check command
# if len(sys.argv) != 2:
#     print(" correct command: python unified_make_dataset_4shapes_remap.py <embedding directory path>")
#     sys.exit(1)

embedding_dir = "./final"
dir_name = os.path.basename(embedding_dir.rstrip("/"))
output_file = f"{dir_name}_dataset.pt"

df = pd.read_csv("./data/sample_dataset.csv")

X, y = [], []

# load embeddings
def load_embedding_desc(drug_name):
    path = os.path.join("./data/biobert_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_tox(drug_name):
    path = os.path.join("./data/biobert_tox_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_smiles(drug_name):
    path = os.path.join("./data/biobert_smiles_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

def load_embedding_pharmaco(drug_name):
    path = os.path.join("./data/biobert_pharmacodynamics_embeddings", f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

# process drug pairs
for _, row in df.iterrows():
    name = row['name']
    label = row['label']
    label = ast.literal_eval(label)
    emb_description = load_embedding_desc(name)
    emb_tox= load_embedding_tox(name)
    emb_smiles = load_embedding_smiles(name)
    emb_pharmaco = load_embedding_pharmaco(name)

    if emb_description is None or emb_tox is None or emb_smiles is None or emb_pharmaco is None:
        continue

    X.append(emb_description)
    X.append(emb_tox)
    X.append(emb_smiles)
    X.append(emb_pharmaco)
    y.append(label)
    
# convert to tensor
X = torch.stack(X)
y = torch.tensor(y)

# remap index
# y_remapped = y.clone()
# y_remapped[y >= 76] -= 1

# print summary
print(f"\n completed making dataset!")
print(f" - original number of index: {len(torch.unique(y))}")
# print(f" - after remapping: {len(torch.unique(y))}")
print(f" - list of index: {torch.unique(y).tolist()}")

# save file
torch.save((X, y), output_file)
print(f"\n saved as: {output_file}")