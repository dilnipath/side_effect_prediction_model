import torch
import torch.nn as nn
import torch.optim as optim
import json
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import pandas as pd
import argparse
import os
import keras
import tensorflow

results = []

hidden_dim = 128
dropout = 0.3
lr = 0.001

trainset = torch.load("./train_test_data/data_train.pt")
testset = torch.load("./train_test_data/data_test.pt")
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
X_test = torch.tensor(X_test.detach().clone(), dtype=torch.float32)
y_test = torch.tensor(y_test.detach().clone(), dtype=torch.float32) 

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)
val_loader = DataLoader(TensorDataset(X_val, y_val), batch_size=512)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=512)

model = nn.Sequential(
    nn.Linear(input_dim, input_dim),
    nn.LeakyReLU(),
    nn.Dropout(dropout),
    nn.Linear(input_dim, hidden_dim),
    nn.LeakyReLU(),
    nn.Dropout(dropout),
    nn.Linear(hidden_dim, output_dim)
)

keras.losses.BinaryFocalCrossentropy(
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction="sum_over_batch_size",
    name="binary_focal_crossentropy",
)

optimizer = optim.Adam(model.parameters(), lr=lr)
criterion = keras.losses.BinaryFocalCrossentropy(from_logits=True)  # For multi-label classification

best_recall= 0
patience = 20
wait = 0

for epoch in range(1, 301):
    model.train()
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs.detach().numpy(), y_batch.detach().numpy())
        optimizer.step()

    model.eval()
    y_pred = []
    with torch.no_grad():
        for Xb, _ in val_loader:
            out = model(Xb)
            y_pred.append(torch.sigmoid(out).cpu())  # Apply sigmoid for threshold
    y_pred = torch.cat(y_pred)
    y_pred_binary = (y_pred > 0.5).float()  # Threshold at 0.5

    pred_score = 0
    real_score = 0

    for i in range(len(y_val)):
        for j in range(len(y_val[i])):
            if y_val[i][j] == 1:
                real_score += 1
            if y_val[i][j] == y_pred_binary[i][j] and y_val[i][j] == 1:
                pred_score += 1
    ones_correct = pred_score/real_score

    acc = accuracy_score(y_val.cpu().numpy(), y_pred_binary.numpy())
    precision = precision_score(y_val.cpu().numpy(), y_pred_binary.numpy(), average = "micro")
    recall = recall_score(y_val.cpu().numpy(), y_pred_binary.numpy(), average = "micro")

    print(f"Epoch {epoch}, Val Acc: {acc:.4f}, Ones Correct: {ones_correct:.4f}, Best: {best_recall:.4f}, Precision: {precision:.4f}, Recall: {recall: .4f}, Wait: {wait}/{patience}")

    if recall >= best_recall:
        best_recall = recall
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
test_recall = recall_score(y_test.cpu().numpy(), y_pred_test_binary.numpy(), average = "micro")
print(f"Final Test Recall for: {test_recall:.4f}")

results.append([input_dim, epoch, best_recall, test_recall, precision, acc])

# Save result for each embedding
for result in results:
    emb_name = result[0]
    df_single = pd.DataFrame([result], columns=['Input dim', 'Epochs', 'Best Recall Accuracy', 'Test Recall', 'Precision', 'Accuracy'])
    csv_path = "model_result.csv"
    df_single.to_csv(csv_path, index=False)
    print(f"Saved result as model_result.csv")