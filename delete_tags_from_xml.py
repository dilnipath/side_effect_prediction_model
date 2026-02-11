import xml.etree.ElementTree as ET

context = ET.iterparse('full_database.xml', events=('start',))

for event, elem in context:
    if event == 'start':
        if elem.tag == "{http://www.drugbank.ca}product":
            for el in elem.iter():
                el.remove()
            elem.remove()

del context
