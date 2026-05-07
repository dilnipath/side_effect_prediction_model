"""creates bioBERT embeddings of indicated feature"""

import torch
import csv
import os
import random
from transformers import AutoTokenizer, AutoModel


FEATURE_NAME = "half-life"

# Load BioBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModel.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

def chunk_text(text, max_tokens=512):
    start = 0
    tokens = tokenizer.tokenize(text)
    if len(tokens) > max_tokens:
        start = random.randint(0, len(tokens) - max_tokens)
    chunk = tokens[start: start+max_tokens]
    chunk = tokenizer.convert_tokens_to_string(chunk)
    return chunk

def get_biobert_embeddings(text):
    embeddings = []
    chunk = chunk_text(text)
    inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze()  # Use [CLS] token
    embeddings.append(cls_embedding.cpu())
    final_embedding = torch.cat(embeddings, dim=0)
    return final_embedding

output_dir = f"./biobert_{FEATURE_NAME}_embeddings"
os.makedirs(output_dir, exist_ok=True)

saved_count = 0

with open('datasets/sample_dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        drug_description = row[FEATURE_NAME]
        drug_name = row['name']

        try:
            embedding = get_biobert_embeddings(drug_description)
            save_path = os.path.join(output_dir, f"{drug_name}.pt")
            torch.save(embedding, save_path)
            saved_count += 1
            print(f"{drug_name} embedding saved:", save_path)
        except Exception as e:
            print(f"Error processing {drug_name}: {e}")
            continue
