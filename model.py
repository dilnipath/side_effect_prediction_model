import torch
import torch.nn as nn
import torch.optim as optim
import json
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import argparse
import os

results = []

hidden_dim = 128
dropout = 0.3
lr = 0.001

trainset = torch.load("./data/train_test_data/train.pt")
testset = torch.load("./data/train_test_data/test.pt")
X_train_full, y_train_full = trainset[0], trainset[1]
X_test, y_test = testset[0], testset[1]

if y_train_full.min() == 1:
    y_train_full -= 1
    y_test -= 1

input_dim = X_train_full.shape[1]
output_dim = 685

X_train_np = X_train_full.numpy()
y_train_np = y_train_full.numpy()
X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(
    X_train_np, y_train_np, test_size=0.2, random_state=42
)

X_train = torch.tensor(X_train_split, dtype=torch.float32) 
y_train = torch.tensor(y_train_split, dtype=torch.float32) 
X_val = torch.tensor(X_val_split, dtype=torch.float32) 
y_val = torch.tensor(y_val_split, dtype=torch.float32) 
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32) 

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)
val_loader = DataLoader(TensorDataset(X_val, y_val), batch_size=512)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=512)

model = nn.Sequential(
    nn.Linear(input_dim, input_dim),
    nn.ReLU(),
    nn.Dropout(dropout),
    nn.Linear(input_dim, hidden_dim),
    nn.ReLU(),
    nn.Dropout(dropout),
    nn.Linear(hidden_dim, output_dim)
)

optimizer = optim.Adam(model.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()  # For multi-label classification

best_val_acc = 0
patience = 20
wait = 0

for epoch in range(1, 301):
    model.train()
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()

    model.eval()
    y_pred = []
    with torch.no_grad():
        for Xb, _ in val_loader:
            out = model(Xb)
            y_pred.append(torch.sigmoid(out).cpu())  # Apply sigmoid for threshold
    y_pred = torch.cat(y_pred)
    y_pred_binary = (y_pred > 0.5).float()  # Threshold at 0.5
    acc = accuracy_score(y_val.cpu().numpy(), y_pred_binary.numpy())

    print(f"Epoch {epoch}, Val Acc: {acc:.4f}, Best: {best_val_acc:.4f}, Wait: {wait}/{patience}")

    if acc >= best_val_acc:
        best_val_acc = acc
        wait = 0
        save_model_path = "best_model.pth"
        torch.save(model.state_dict(), save_model_path)
    else:
        if epoch >= 200:
            wait += 1

    if wait >= patience:
        print("Early stopping triggered.")
        break

model.eval()
y_pred_test = []
with torch.no_grad():
    for Xb, _ in test_loader:
        out = model(Xb)
        y_pred_test.append(torch.sigmoid(out).cpu())  # Apply sigmoid for threshold
y_pred_test = torch.cat(y_pred_test)
print(y_pred_test)
y_pred_test_binary = (y_pred_test > 0.5).float()  # Threshold at 0.5
print(y_pred_test_binary)
test_acc = accuracy_score(y_test.cpu().numpy(), y_pred_test_binary.numpy())
print(f"Final Test Accuracy for: {test_acc:.4f}")

results.append([input_dim, epoch, best_val_acc, test_acc])

# Save result for each embedding
for result in results:
    emb_name = result[0]
    df_single = pd.DataFrame([result], columns=['Input dim', 'Epochs', 'Best Val Accuracy', 'Test Accuracy'])
    csv_path = "model_result.csv"
    df_single.to_csv(csv_path, index=False)
    print(f"Saved result as model_result.csv")