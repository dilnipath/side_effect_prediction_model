import requests
from bs4 import BeautifulSoup
import csv

base = "https://medlineplus.gov/druginfo/meds/"
headers = {"User-Agent": "Mozilla/5.0"}

drug_texts = []
keys = []

with open('data/drug_keys.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        keys.append(row[0])

for key in keys:
    url = base + key + ".html"

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Failed:", key)
        continue

    soup = BeautifulSoup(r.text, "html.parser")

    # main content block
    container = soup.find("article")
    if not container:
        continue

    text = ""

    name = soup.find("h1", "with-also").get_text(" ", strip=True)

    drug_texts.append({
        "key": key,
        "name": name,
    })

    with open('data/drug_keys.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['key', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(drug_texts)