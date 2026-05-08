import pandas as pd
import csv

side_effects_df = pd.read_csv('./datasets/fewshot_side_effects_nodups.csv')
full_df = pd.read_csv('./datasets/drug_side_effects_full.csv')
match_names_df = pd.read_csv('./datasets/match_names.csv')

# # Create a dictionary for quick lookup
# key_to_db_name = dict(zip(match_names_df['ml_name'], match_names_df['db_name']))

# # Add db_name column by mapping
# side_effects_df['db_name'] = side_effects_df['ml_name'].map(key_to_db_name)

# side_effects_df.to_csv('./datasets/fewshot_2.csv', index=False)

# s

# names = {}
# for i, row in side_effects_df.iterrows():
#     if row["ml_name"] in names:
#         names[row["ml_name"]] += 1
#         print(row["ml_name"])
#     else:
#         names[row["ml_name"]] = 1


# side_effects_df.to_csv("./datasets/names_nodups.csv", index=False)
# missing = []
# ml_names = set(side_effects_df["ml_name"])
# db_names = set(side_effects_df["ml"])
# for i, row in match_names_df.iterrows():
#     d = {}
#     if row["ml_name"] not in ml_names:
#         name = row["ml_name"]
#         d["ml_key"] = row["ml_key"]
#         d["ml_name"] = row["ml_name"]
#         d["db_name"] = row["db_name"]
#         row = full_df.loc[name, "side_effects"]
#         d["side_effects"] = row["side_effects"]
#         missing.append(d)

# with open("datasets/missing_names.csv", "w", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     headers = ["ml_key", "ml_name"]

dups = ["Abacavir", "Abiraterone", "Adefovir", "Albendazole", "Allopurinol", "Aripiprazole", "Atenolol", "Baclofen", "Benazepril", "Betaine", "Bicalutamide", "Candesartan", "Dabigatran", "Diclofenac", "Digoxin", "Dinoprostone", "Eflornithine", "Enalapril", "Enzalutamide", "Epirubicin", "Eslicarbazepine", "Estramustine", "Etoposide", "Fosinopril", "Gabapentin", "Ibuprofen", "Imipramine", "Indapamide", "Lansoprazole", "Levofloxacin", "Liothyronine", "Loperamide", "Mefloquine", "Megestrol", "Melphalan", "Metformin", "Metronidazole", "Mitomycin", "Moexipril", "Morphine", "Naproxen", "Niacin", "Olaparib", "Oseltamivir", "Oxazepam", "Perindopril", "Perphenazine", "Piroxicam", "Potassium Iodide", "Prednisone", "Quinapril", "Ramipril", "Ranitidine", "Rifampin", "Risperidone", "Selegiline", "Simvastatin", "Spironolactone", "Tacrolimus", "Tamoxifen", "Telmisartan", "Temozolomide", "Topiramate", "Tramadol", "Valproate", "Warfarin"]
for i, row in side_effects_df.iterrows():
    if row["ml_name"] in dups:
        side_effects_df.at[i, "db_name"] = row["ml_name"]

side_effects_df.to_csv('./datasets/fewshot_2.csv', index=False)