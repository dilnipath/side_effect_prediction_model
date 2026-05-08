"""Utilizes Claude AI API to split side effects into smallest possible units. Ex: 'difficulty breathing and swallowing' --> ['difficulty breathing', 'difficult swallowing']"""

import csv
import anthropic
import pandas as pd
from dotenv import load_dotenv
load_dotenv() 

client = anthropic.Anthropic()

drug_df = pd.read_csv("./datasets/drug_side_effects_full.csv", encoding = "utf-8")
ml_names = drug_df[1250:]["ml_name"]
db_names = drug_df[1250:]["db_name"]
side_effects = drug_df[1250:]["side_effects"]

split_side_effects = []
4
with open("datasets/fewshot_side_effects.csv", "a", encoding = "utf-8") as csvfile:
    fieldnames = ["ml_name", "side_effects", "db_name"]
    writer = csv.DictWriter(csvfile, fieldnames)
    # writer.writeheader()
    for i in range(1250, 1399):
        dict1 = {}
        message = client.messages.create(
            model='claude-opus-4-5',
            max_tokens=1000,
            messages=[
                {
                    'role': 'user',
                    'content': f"I am going to give you drugs names and their corresponding side effects in a list format. I want you to return those side effects in a list format matching the one we gave you but split each side effect into the smallest possible unit that still makes sense. Do not include anything except for the list in the response. For example, ['swelling of the face, throat, tongue, lips, eyes'] becomes '['swelling of the face', 'swelling of the throat', 'swelling of the tongue', 'swelling of the lips', 'swelling of the eyes']'. ['rash; hives; hoarseness;'] becomes '['rash', 'hives', 'hoarseness']'. ['fever, cough,  or other signs of infection'] becomes '['fever', 'cough', 'signs of infection']'. If a side effect includes the drug name, replace it with 'this medication' instead. This is the drug {ml_names[i]} and its side effects are {side_effects[i]}.",
                }
            ],
        )
        dict1["ml_name"] = ml_names[i]
        dict1["db_name"] = db_names[i]
        dict1["side_effects"] = message.content[0].text.strip()
        
        split_side_effects.append(dict1)

        writer.writerow(dict1)

