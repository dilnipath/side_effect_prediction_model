"""Collects side effects from MedlinePlus"""

import requests
from bs4 import BeautifulSoup
import csv

base = "https://medlineplus.gov/druginfo/meds/a"
headers = {"User-Agent": "Mozilla/5.0"}

drug_texts = []
keys = []

with open('././datasets/match_names.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        keys.append(row[2])

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
    print(name)
    if soup.find("div", "section-body", id="section-side-effects"):
        side_effects = [p.get_text(" ", strip=True) for p in soup.find("div", "section-body", id="section-side-effects").find_all("li")]
    else:
        print("no side effects found for:", name)
        continue

    drug_texts.append({
        "key": key,
        "name": name,
        "side_effects": side_effects
    })

with open('././datasets/drug_side_effects_full.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['key', 'name', 'side_effects']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(drug_texts)