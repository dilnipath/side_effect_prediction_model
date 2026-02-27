import csv
import ast
import pandas as pd

all_side_effects = {}

labels_ordered = open('data/labels_order.txt', 'r').read()
labels_ordered = ast.literal_eval(labels_ordered)

split_df = pd.read_csv('data/split_side_effects.csv')
split_df["name"] = split_df["name"].str.lower()

labels_lst = []

for _, row in split_df.iterrows():
    side_effects = row[4]
    side_effects = ast.literal_eval(side_effects)
    label = [0] * len(labels_ordered)
    for s in side_effects:
        index = labels_ordered.index(s)
        if index != -1:
            label[index] = 1
    labels_lst.append(label)

split_df['labels'] = labels_lst

features_df = pd.read_csv('data/features.csv')
features_df["name"] = features_df["name"].str.lower()

# print(features_df.shape)
# print(split_df.shape)

df_merged = pd.merge(features_df, split_df[["name", "labels"]], on="name")

df_merged.to_csv('data/sample_dataset.csv', index=False)
