import xml.etree.ElementTree as ET
import csv
import pandas as pd

context = ET.iterparse('full_database.xml', events=('start',))

lst = []

drug_names_df = pd.read_csv('drug_keys_copy.csv')
drug_names = drug_names_df['name'].tolist()


i = 0
for event, elem in context:
    if event == 'start':
        if elem.tag == "{http://www.drugbank.ca}drug":
            name = elem.find("{http://www.drugbank.ca}name")
            description = elem.find("{http://www.drugbank.ca}description")
            tox = elem.find("{http://www.drugbank.ca}toxicity")

            properties = elem.find("{http://www.drugbank.ca}calculated-properties")
        
            dict1 = {}
            
            if name is not None and name.text in drug_names:
                print(name.text)
                dict1["name"] = name.text
                
                if description is not None:
                    dict1["description"] = description.text
                else: 
                    dict1["description"] = -1
                    
                if tox is not None:
                    dict1["toxicity"] = tox.text
                else:
                    dict1["toxicity"] = -1

                if properties is not None:
                    for prop in properties:
                        if prop.text is None or prop is None:
                            continue
                        else:
                            kind = (prop.find("{http://www.drugbank.ca}kind"))
                            value = (prop.find("{http://www.drugbank.ca}value"))
    
                            if kind is not None and value is not None:
                                if kind.text == "SMILES":
                                    dict1["SMILES"] = value.text
                else:
                    dict1["SMILES"] = -1

                print(dict1["name"])
                lst.append(dict1)
            
                i += 1
                print(f"Processed drug {i}: {name.text}")

        elem.clear()
        
        if i == 1000:
            break

del context

with open("sample_data.csv", 'w', newline = '', encoding='utf-8') as csvfile:
    fieldnames = ["name", "description", "toxicity", "SMILES"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(lst)