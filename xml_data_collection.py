import xml.etree.ElementTree as ET
import csv
import pandas as pd

context = ET.iterparse('side_effect_prediction_model/full database.xml', events=('start', 'end'))

lst = []

drug_names_df = pd.read_csv('side_effect_prediction_model/data/drug_keys_copy.csv')
drug_names = drug_names_df['name'].tolist()

desired_drug = False
processed_Drugs = []
drug_dict = {}
since_drug_tag = 0
count_since_drug_tag = False
for event, elem in context:

    #ifi find name we want, toggle true
    #if run into desired tag, grab it
    #next drug tag, toggle false
    if event == 'start':
        if elem.tag == "{http://www.drugbank.ca}drug":
            count_since_drug_tag = True

        if count_since_drug_tag:
             since_drug_tag += 1

        if elem.tag == "{http://www.drugbank.ca}name" and since_drug_tag <= 10:
            name = elem
            if name is not None and name.text in drug_names:
                desired_drug = True
                drug_dict["name"] = name.text
                description = elem.find("{http://www.drugbank.ca}description")
                text = description

        if desired_drug:
            if elem.tag == "{http://www.drugbank.ca}description" and "description" not in drug_dict:
                if elem.text is not None:
                    text = elem.text.replace(",", "").replace("\n", "").replace("\r", "").replace("\t", "")
                    drug_dict["description"] = text
                else:
                    drug_dict["description"] = -1
            if elem.tag == "{http://www.drugbank.ca}toxicity" and "toxicity" not in drug_dict:
                if elem.text is not None:
                    text = elem.text.replace(",", "").replace("\n", "").replace("\r", "").replace("\t", "")
                    drug_dict["toxicity"] = text
                else:
                    drug_dict["toxicity"] = -1
            if elem.tag == '{http://www.drugbank.ca}calculated-properties' and "SMILES" not in drug_dict:
                for prop in elem:
                    if prop.text is None or prop is None:
                        continue
                    else:
                        kind = (prop.find("{http://www.drugbank.ca}kind"))
                        value = (prop.find("{http://www.drugbank.ca}value"))

                        if kind is not None and value is not None:
                            if kind.text == "SMILES":
                                drug_dict["SMILES"] = value.text
                if "SMILES" not in drug_dict:
                    drug_dict["SMILES"] = -1

    if event == 'end':
        if elem.tag == "{http://www.drugbank.ca}drug":
            since_drug_tag = 0
            count_since_drug_tag = False
            if desired_drug:
                desired_drug = False
                processed_Drugs.append(drug_dict)
                print(f"Processed drug: {drug_dict['name']}")
                drug_dict = {}

        elem.clear()

del context

with open("side_effect_prediction_model/data/sample_data.csv", 'w', newline = '',  encoding='utf-8') as csvfile:
    fieldnames = ["name", "description", "toxicity", "SMILES"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(processed_Drugs)