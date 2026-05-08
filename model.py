import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import json
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import pandas as pd
import argparse
import os

torch.manual_seed(900)

class BinaryFocalLoss(nn.Module):
    def __init__(self, gamma=2.0, alpha=0.25):
        super().__init__()
        self.gamma = gamma
        self.alpha = alpha

    def forward(self, logits, targets):
        # Standard BCE computed on raw logits (numerically stable)
        bce = F.binary_cross_entropy_with_logits(logits, targets, reduction='none')
        # Convert logits to probabilities to compute the focal weight
        probs = torch.sigmoid(logits)
        # p_t is the model's confidence in the correct class
        p_t = probs * targets + (1 - probs) * (1 - targets)
        # alpha_t balances positive/negative contributions
        alpha_t = self.alpha * targets + (1 - self.alpha) * (1 - targets)
        # Focal weight: (1 - p_t)^gamma reduces loss for easy examples
        focal_weight = alpha_t * (1 - p_t) ** self.gamma
        return (focal_weight * bce).mean()


results = []

hidden_dim = 256
dropout = 0.5  
lr = 0.1      
batch_size = 16 

trainset = torch.load("./train_test_data/train_general.pt")
testset = torch.load("./train_test_data/test_general.pt")
X_train_full, y_train_full = trainset[0], trainset[1]
X_test, y_test = testset[0], testset[1]


input_dim = X_train_full.shape[1]
output_dim = 2888

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

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=batch_size, shuffle=True)
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

optimizer = optim.Adagrad(model.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss(weight= torch.tensor(25))  # Pure PyTorch focal loss

best_recall = 0
patience = 20
wait = 0


for epoch in range(1, 301):
    model.train()
    loss_total = 0
    for X_batch, y_batch in train_loader:   
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)  # outputs kept in graph (no .detach())
        loss.backward()
        loss_total+=loss.item()                    # compute gradients — was missing
        optimizer.step()
        # print("Loss", loss.item())
    model.eval()
    y_pred = []
    with torch.no_grad():
        for Xb, _ in val_loader:
            out = model(Xb)
            y_pred.append(torch.sigmoid(out).cpu())
    y_pred = torch.cat(y_pred)
    y_pred_binary = (y_pred > 0.5).float()
    print(loss_total/len(X_batch))
    loss_total = 0

    acc = accuracy_score(y_val.cpu().numpy(), y_pred_binary.numpy())
    precision = precision_score(y_val.cpu().numpy(), y_pred_binary.numpy(), average="micro", zero_division=0)
    recall = recall_score(y_val.cpu().numpy(), y_pred_binary.numpy(), average="micro", zero_division=0)

    print(f"Epoch {epoch}, Val Acc: {acc:.4f}, Best: {best_recall:.4f}, Precision: {precision:.4f}, Recall: {recall:.10f}, Wait: {wait}/{patience}")

    if recall >= best_recall:
        best_recall = recall
        wait = 0
        torch.save(model.state_dict(), "best_model.pth")
    else:
        wait += 1  # was: if epoch >= 200: wait += 1

    if wait >= patience:
        print("Early stopping triggered.")
        break

model.eval()
y_pred_test = []
with torch.no_grad():
    for Xb, _ in test_loader:
        out = model(Xb)
        y_pred_test.append(torch.sigmoid(out).cpu())
y_pred_test = torch.cat(y_pred_test)
y_pred_test_binary = (y_pred_test > 0.5).float()
test_recall = recall_score(y_test.cpu().numpy(), y_pred_test_binary.numpy(), average="micro", zero_division=0)
print(f"Final Test Recall: {test_recall:.4f}")

results.append([input_dim, epoch, best_recall, test_recall, precision, acc])

for result in results:
    emb_name = result[0]
    df_single = pd.DataFrame([result], columns=['Input dim', 'Epochs', 'Best Recall Accuracy', 'Test Recall', 'Precision', 'Accuracy'])
    csv_path = "model_result.csv"
    df_single.to_csv(csv_path, index=False)
    print(f"Saved result as model_result.csv")