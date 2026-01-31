import xml.etree.ElementTree as ET

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
                newlst = []
                newlst.append(name.text)
                newlst.append(description.text)
                newlst.append(tox.text)

                for prop in properties:
                    if (prop.find("{http://www.drugbank.ca}kind")).text == "logP":
                        newlst.append((prop.find("{http://www.drugbank.ca}value")).text)

                lst.append(newlst)
                
                i += 1
                print(f"Processed drug {i}: {name.text}")

        elem.clear()
        
        if i == 2:
            break

del context

print(lst)