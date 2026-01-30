import xml.etree.ElementTree as ET

# print("parsing")
# tree = ET.parse('full_database.xml')
# root = tree.getroot()

# print("here")

# i = 0
# for child in root:
#     print("inside")
#     print(child.tag, child.attrib)
#     if i == 10:
#         break

context = ET.iterparse('full_database.xml', events=('start',))

lst = []

i = 0
for event, elem in context:
    print(elem.text)
    if event == 'start':
        if elem.tag == "{http://www.drugbank.ca}drug":
            
            newlst = []
            name = elem.find("{http://www.drugbank.ca}name")
            newlst.append(name.text)
            
            description = elem.find("{http://www.drugbank.ca}description")
            newlst.append(description.text)
            
            tox = elem.find("{http://www.drugbank.ca}toxicity")
            newlst.append(tox.text)

            lst.append(newlst)
            
            i += 1

        elem.clear()
        
        if i == 2:
            break

del context

print(lst)