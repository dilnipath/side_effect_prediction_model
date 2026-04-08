import csv
import ast
import pandas as pd

df = pd.read_csv('././datasets/fewshot_side_effects.csv')

all_side_effects = []

# dict1 = {}

# for j,row in df.iterrows():
#     # if row["name"] == "Atezolizumab Injection":
#     #     continue
#     side_effects = row["side_effects"]
#     side_effects = ast.literal_eval(side_effects)
#     for i in side_effects:
#         if i not in all_side_effects:
#             all_side_effects.append(i)
#         if i not in dict1.keys():
#             dict1[i] = 1
#         else:
#             dict1[i] += 1

# print(sorted(dict1.items(), key=lambda item: item[1]))

# with open('label_order_250.txt', 'w') as f:
#     for item in all_side_effects:
#         f.write(f"'{item}',")


labels_ordered = open("./create_multilabel_dataset/label_order_251.txt").read()

split_df = pd.read_csv('./datasets/fewshot_side_effects.csv')
split_df["db_name"] = split_df["db_name"].str.lower()

labels_lst = []

for _, row in split_df.iterrows():
    print(row["db_name"])
    side_effects = row["side_effects"]
    side_effects = ast.literal_eval(side_effects)
    label = [0] * len(labels_ordered)
    for s in side_effects:
        index = labels_ordered.index(s)
        if index != -1:
            label[index] = 1
    labels_lst.append(label)

split_df['labels'] = labels_lst

xml_df = pd.read_csv('./datasets/matched_names_xml_data.csv')
xml_df["db_name"] = xml_df["db_name"].str.lower()

df_merged = pd.merge(xml_df, split_df[["db_name", "ml_name", "labels"]], on="db_name")

df_merged.to_csv('./datasets/251_dataset.csv', index=False)
