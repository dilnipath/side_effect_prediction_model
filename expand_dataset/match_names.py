import csv

drugbank_names = set()
with open("./datasets/xml_drug_names.csv", 'r', newline='', encoding='utf-8') as drugbank:
    reader = csv.reader(drugbank)
    next(reader, None)
    for row in reader:
        drugbank_names.add(row[0])

medline_names = set()
medline_names_ids = {}
with open("./datasets/medline_names.csv", 'r', newline='', encoding='utf-8') as medline:
    reader = csv.reader(medline)
    next(reader, None)
    for row in reader:
        medline_names.add(row[1])
        medline_names_ids[row[1]] = row[0]

shared_names = []
possible_substring = []
for name in drugbank_names:
    if name in medline_names:
        shared_names.append(name)
    elif name:
        possible_substring.append(name)

all_substring_names_db = []
all_substring_names_ml = []
for db_name in possible_substring:
    for ml_name in medline_names:
        if (db_name in ml_name or ml_name in db_name) and ml_name.find( " and ") == -1:
            all_substring_names_db.append(db_name)
            all_substring_names_ml.append(ml_name)

# delete rows in which db substrings appear in longer ml names multiple times
substring_db = []
substring_ml = []
for i, substring in enumerate(all_substring_names_db):
    count = all_substring_names_db.count(substring)
    if count == 1:
        substring_db.append(substring)
        substring_ml.append(all_substring_names_ml[i])

final_substring_db = []
final_substring_ml = []
for i, substring in enumerate(substring_ml):
    count = substring_ml.count(substring)
    if count == 1:
        final_substring_ml.append(substring)
        final_substring_db.append(substring_db[i])

with open('./datasets/match_names.csv', 'w', newline='', encoding='utf-8') as match:
    writer = csv.writer(match)
    field_names = ['ml_name', 'db_name', 'ml_key']
    writer.writerow(field_names)
    for name in shared_names:
        writer.writerow([name, name, medline_names_ids[name]])
    for i in range(len(final_substring_db)):
        writer.writerow([final_substring_db[i], final_substring_ml[i], medline_names_ids[final_substring_ml[i]]])
