import csv
import ast
import pandas as pd

df = pd.read_csv('././datasets/fewshot_side_effects.csv')

all_side_effects = []

dict1 = {}

for j,row in df.iterrows():
    # if row["name"] == "Atezolizumab Injection":
    #     continue
    side_effects = row["side_effects"]
    print(row["ml_name"])
    side_effects = ast.literal_eval(side_effects)
    for i in side_effects:
        if i not in all_side_effects:
            all_side_effects.append(i)
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] += 1

print(sorted(dict1.items(), key=lambda item: item[1]))

with open('label_order_251.txt', 'w') as f:
    for item in all_side_effects:
        f.write(f"'{item}',")
