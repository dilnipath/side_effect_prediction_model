"""Collecting names of all drugs in the DrugBank Database"""

import xml.etree.ElementTree as ET
import csv
import pandas as pd

context = ET.iterparse('full database.xml', events=('start', 'end'))

lst = []

processed_Drugs = []
drug_dict = {}
since_drug_tag = 0
count_since_drug_tag = False
for event, elem in context:

    if event == 'start':
        if elem.tag == "{http://www.drugbank.ca}drug":
            count_since_drug_tag = True

        if count_since_drug_tag:
            since_drug_tag += 1

        if elem.tag == "{http://www.drugbank.ca}name" and since_drug_tag <= 10:
            name = elem
            if name is not None:
                drug_dict["name"] = name.text

    if event == 'end':
        if elem.tag == "{http://www.drugbank.ca}drug":
            since_drug_tag = 0
            count_since_drug_tag = False
            if len(drug_dict) != 0:
                processed_Drugs.append(drug_dict)
                print(f"Processed drug: {drug_dict['name']}")
            drug_dict = {}

        elem.clear()

del context

with open("./datasets/xml_drug_names.csv", 'w', newline = '',  encoding='utf-8') as csvfile:
    fieldnames = ["name"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(processed_Drugs)