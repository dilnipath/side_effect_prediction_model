import requests
from bs4 import BeautifulSoup
import csv

base = "https://medlineplus.gov/druginfo/meds/"
headers = {"User-Agent": "Mozilla/5.0"}

drug_texts = []
keys = []

with open('side_effect_prediction_model/data/drug_keys.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        keys.append(row[0])
        if i == 100:
            break
        i += 1

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
    side_effects = [p.get_text(" ", strip=True) for p in soup.find("div", "section-body", id="section-side-effects").find_all("li")]

    drug_texts.append({
        "key": key,
        "name": name,
        "side_effects": side_effects
    })

    with open('side_effect_prediction_model/data/drug_side_effects.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['key', 'name', 'side_effects']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(drug_texts)