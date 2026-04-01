import csv
import anthropic
import pandas as pd
from dotenv import load_dotenv
load_dotenv()  # must be called before anthropic.Anthropic()

client = anthropic.Anthropic()

drug_df = pd.read_csv("./datasets/full_drug_side_effects.csv", encoding = "utf-8")
names = drug_df[100:110]["name"]
side_effects = drug_df[100:110]["side_effects"]

split_side_effects = []

for 100 in range(110):
    dict1 = {}
    message = client.messages.create(
        model='claude-opus-4-5',
        max_tokens=1000,
        messages=[
            {
                'role': 'user',
                'content': f"I am going to give you drugs names and their corresponding side effects in a list format. I want you to return those side effects in a list format matching the one we gave you but split each side effect into the smallest possible unit that still makes sense. Do not include anything except for the list in the response. For example, ['swelling of the face, throat, tongue, lips, eyes'] becomes '['swelling of the face', 'swelling of the throat', 'swelling of the tongue', 'swelling of the lips', 'swelling of the eyes']'. ['rash; hives; hoarseness;'] becomes '['rash', 'hives', 'hoarseness']'. ['fever, cough,  or other signs of infection'] becomes '['fever', 'cough', 'signs of infection']'. This is the drug {names[i]} and its side effects are {side_effects[i]}.",
            }
        ],
    )
    print(i)
    dict1["name"] = names[i]
    dict1["side_effects"] = message.content[0].text
    split_side_effects.append(dict1)

# fewshot_side_effects = pd.DataFrame(split_side_effects)
# print(fewshot_side_effects)
# fewshot_side_effects.to_csv("datasets/fewshot_side_effects.csv", index = False)

with open("datasets/fewshot_side_effects.csv", "a", encoding = "utf-8") as csvfile:
    fieldnames = ["name", "side_effects"]
    writer = csv.DictWriter(csvfile, fieldnames)
    #writer.writeheader()
    writer.writerows(split_side_effects)