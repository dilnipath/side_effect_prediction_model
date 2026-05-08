"""Splits dataset.pt into training and testing pt files"""

import torch
import sys
import os
import numpy as np
from sklearn.model_selection import train_test_split

input_path = "./datasets/"
base_name = os.path.splitext(os.path.basename(input_path))[0]
output_dir = os.path.dirname(input_path)

data = torch.load("./datasets/dataset.pt")

# check data structure
X, y = data
has_ids = False

# train:test=8:2
train_idx, test_idx = train_test_split(
    range(len(y)), test_size=0.2, random_state=42,
)

# split
X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

# save paths
train_file = os.path.join(output_dir, "train.pt")
test_file  = os.path.join(output_dir, "test.pt")

# save files
torch.save((X_train, y_train), train_file)
torch.save((X_test, y_test), test_file)

# print summary
print(f"completed spliting dataset!")
print(f" - input            : {input_path}")
print(f" - Train set saved  : {train_file} ({X_train.shape[0]} samples)")
print(f" - Test set saved   : {test_file}  ({X_test.shape[0]} samples)")