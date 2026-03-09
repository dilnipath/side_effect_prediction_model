import ast
import os
import sys
import torch
import pandas as pd

# # check command
# if len(sys.argv) != 2:
#     print(" correct command: python unified_make_dataset_4shapes_remap.py <embedding directory path>")
#     sys.exit(1)

embedding_dir = "./data/biobert_embeddings"
dir_name = os.path.basename(embedding_dir.rstrip("/"))
output_file = f"{dir_name}_dataset2.pt"

df = pd.read_csv("./data/sample_dataset.csv")

X, y = [], []

# load embeddings
def load_embedding(drug_name):
    path = os.path.join(embedding_dir, f"{drug_name}.pt")
    return torch.load(path) if os.path.exists(path) else None

# process drug pairs
for _, row in df.iterrows():
    name = row['name']
    label = row['label']
    label = ast.literal_eval(label)
    emb_description = load_embedding(name)

    if emb_description is None:
        continue

    X.append(emb_description)
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