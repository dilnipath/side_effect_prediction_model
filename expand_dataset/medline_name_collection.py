import requests
from bs4 import BeautifulSoup
import csv

base = "https://medlineplus.gov/druginfo/meds/a"
headers = {"User-Agent": "Mozilla/5.0"}

names = []

for i in range(655000, 658000):
    url = base + str(i) + ".html"

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print("Success:", i)
    else:
        print("Failed", i)
        continue


    soup = BeautifulSoup(r.text, "html.parser")

    # main content block
    container = soup.find("article")
    if not container:
        continue

    if soup.find("h1", "with-also"):
        name = soup.find("h1", "with-also").get_text(" ", strip=True)

        names.append({
            "key": i,
            "name": name,
        })

with open('./datasets/medline_names.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['key', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerows(names)