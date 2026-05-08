"""Using generalization_record.txt, generalizes side effects then creates multi-label classification for each drug"""

import csv
import ast
import pandas as pd

df = pd.read_csv('././datasets/match_names_fewshot_side_effects.csv')

all_side_effects = []

with open('./create_multilabel_dataset/processing_side_effects/generalization_record.txt', 'r') as file:
    content = file.read()
    generalized = ast.literal_eval(content)

labels_ordered = open("./create_multilabel_dataset/label_order_full.txt").read()

split_df = pd.read_csv('./datasets/match_names_fewshot_side_effects.csv')
split_df["db_name"] = split_df["db_name"].str.lower()

labels_lst = []

for _, row in split_df.iterrows():
    print(row["db_name"])
    side_effects = row["side_effects"]
    side_effects = ast.literal_eval(side_effects)
    general_side_effects = []
    for i in range(len(side_effects)):
        inlst = False
        for lst in generalized.keys():
            if side_effects[i] in lst:
                if generalized[lst] not in general_side_effects:
                    general_side_effects.append(generalized[lst])
                inlst = True
        if inlst == False:
            general_side_effects.append(side_effects[i])
    labels = ast.literal_eval(labels_ordered)
    label = [0] * len(labels)
    for s in general_side_effects:
        index = labels.index(s)
        if index != -1:
            label[index] = 1
    labels_lst.append(label)

split_df['labels'] = labels_lst

xml_df = pd.read_csv('./datasets/match_names_drugbank_features.csv')
xml_df["db_name"] = xml_df["db_name"].str.lower()

df_merged = pd.merge(xml_df, split_df[["db_name", "ml_name", "labels"]], on="db_name")

df_merged.to_csv('./datasets/full_dataset.csv', index=False)
