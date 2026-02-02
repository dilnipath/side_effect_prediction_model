import xml.etree.ElementTree as ET
import csv

# print("parsing")
# tree = ET.parse('full_database.xml')
# root = tree.getroot()

# print("here")

# i = 0
# for child in root:
#     print("inside")
#     print(child.text, child.attrib)
#     if i == 10:
#         break

context = ET.iterparse('full_database.xml', events=('start',))

lst = []

i = 0
for event, elem in context:
    if event == 'start':
        if elem.tag == "{http://www.drugbank.ca}drug":
            # Only process outer drug elements that have name, description, and toxicity
            name = elem.find("{http://www.drugbank.ca}name")
            description = elem.find("{http://www.drugbank.ca}description")
            tox = elem.find("{http://www.drugbank.ca}toxicity")

            properties = elem.find("{http://www.drugbank.ca}calculated-properties")
            
            # Skip if this is a nested drug in drug-interactions (won't have these attributes)
            if name is not None and description is not None and tox is not None and properties is not None:
                dict1 = {}
                dict1["name"] = name.text
                dict1["description"] = description.text
                dict1["toxicity"] = tox.text

                for prop in properties:

                    if prop.text is None or prop is None:
                        continue
                    else:
                        kind = (prop.find("{http://www.drugbank.ca}kind"))
                        value = (prop.find("{http://www.drugbank.ca}value"))

                        if kind is not None and value is not None:
                            if kind.text == "logP":
                                dict1["logP"] = value.text
                            if kind.text == "SMILES":
                                dict1["SMILES"] = value.text

                    
                    # elif (prop.find("{http://www.drugbank.ca}kind")).text == "logP":
                    #     newlst.append((prop.find("{http://www.drugbank.ca}value")).text)
                    # elif (prop.find("{http://www.drugbank.ca}kind")).text == "SMILES":
                    #     newlst.append((prop.find("{http://www.drugbank.ca}value")).text)

                lst.append(dict1)
                
                i += 1
                print(f"Processed drug {i}: {name.text}")

        elem.clear()
        
        if i == 100:
            break

del context

with open("data/sample_data.csv", 'w', newline = '', encoding='utf-8') as csvfile:
    fieldnames = ["name", "description", "toxicity", "logP", "SMILES"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(lst)