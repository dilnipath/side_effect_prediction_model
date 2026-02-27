import csv
import ast
import pandas as pd

processed_df = pd.read_csv('side_effect_prediction_model/data/drug_side_effects.csv')

processed_side_effects = []

none_split = set()

for _, row in processed_df.iterrows():
    effects = row[2]
    effects = ast.literal_eval(effects)
    processed_drug = []
    for e in effects:
        print(e)
        if e not in none_split:
            split = input("Split?")
            if split == 's':
                lst = e.split(';')
                for j in lst:
                    processed_drug.append(j)
            if split == 'c':
                lst = e.split(',')
                for j in lst:
                    processed_drug.append(j)
            else:
                processed_drug.append(e)
                none_split.add(e)
        else:
                processed_drug.append(e)
    processed_side_effects.append(processed_drug)

processed_df['processed_side_effects'] =  processed_side_effects
print(processed_df['processed_side_effects'])

processed_df.to_csv('split_side_effects.csv')


