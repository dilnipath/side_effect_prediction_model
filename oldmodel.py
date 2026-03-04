import pandas as pd
import random
import numpy as np
from sklearn.model_selection import train_test_split
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from transformers import AutoTokenizer, AutoModel
from transformers import Trainer, TrainingArguments
from datasets import Dataset
from sklearn.metrics import f1_score, accuracy_score, recall_score
import ast as ast

def arg_max(model_preds):
    label_preds = []
    for i in model_preds:
        label_preds.append(np.argmax(i))
    return label_preds

def evaluate(type, labels, preds):
    f1 = f1_score(labels, preds)
    print(f"{type} F1 SCORE: ", f1)
    accuracy = accuracy_score(labels, preds)
    print(f"{type} ACCURACY SCORE: ", accuracy)
    recall = recall_score(labels, preds)
    print(f"{type} RECALL SCORE: ", recall)

def tokenize(batch):
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")

    return tokenizer(
        batch['name'], batch["description"], batch["toxicity"], batch["smiles"],
        truncation=True,
        padding="max_length",
        max_length=512,
    )

def model(fname):
    df = pd.read_csv(fname)

    df['description'] = df["description"].astype(str)
    df['toxicity'] = df["toxicity"].astype(str)
    df['smiles'] = df["smiles"].astype(str)
    #df['label'] = df['label'].str.replace('"', '').replace("'", '')
    #print(type(temp))

    train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)

    val_df, test_df = train_test_split(test_df, test_size=0.5, random_state=0)

    train_ds = Dataset.from_pandas(train_df)
    test_ds = Dataset.from_pandas(test_df)
    val_ds = Dataset.from_pandas(val_df)


    # for index, row in df.iterrows(): --> check if there is anything that is possibly greater than 512 characters
    #     sentence = row["sentence"]
    #     beginning = random.randint(0, len(sentence) - 512)
    #     truncated_sentence = sentence[beginning:beginning + 512]
    #     df.at[index, "sentence"] = truncated_sentence

    train_ds = train_ds.map(tokenize, batched=True)
    test_ds = test_ds.map(tokenize, batched=True)
    val_ds = val_ds.map(tokenize, batched=True)

    #Set format for PyTorch
    train_ds.set_format("torch")
    test_ds.set_format("torch")
    val_ds.set_format("torch")

    print(train_ds[0]['input_ids'])

    for row in train_ds:
        row['label'] = ast.literal_eval(row['label'])
    for row in test_ds:
        row['label'] = ast.literal_eval(row['label'])
    for row in val_ds:
        row['label'] = ast.literal_eval(row['label'])
    numoflabels = train_ds['label'][2]

    m = AutoModel.from_pretrained("dmis-lab/biobert-v1.1", num_labels=len(numoflabels))

    m(train_ds[0]['input_ids'])



    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        logging_steps=20,
        evaluation_strategy="epoch",
    )

    trainer = Trainer(
        model=m,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
    )

    trainer.train()

    train_preds, train_label_ids, train_metrics = trainer.predict(train_ds)
    preds = arg_max(train_preds)
    evaluate("train", train_df["label"], preds)

    val_preds, val_label_ids, val_metrics = trainer.predict(val_ds)
    preds = arg_max(val_preds)
    evaluate("val", val_df["label"], preds)

    test_preds, test_label_ids, test_metrics = trainer.predict(test_ds)
    preds = arg_max(test_preds)
    evaluate("test", test_df["label"], preds)

def main():
    model("data/minidata.csv")

main()