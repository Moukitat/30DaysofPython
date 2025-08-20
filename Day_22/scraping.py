# Exercice Jour22

import requests
from bs4 import BeautifulSoup
import json

# 1-)
url_bu = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url_bu)
soup = BeautifulSoup(response.text, "html.parser")

stats_div = soup.find("div", class_="entry-content")

data_bu = {}

if stats_div:
    paragraphs = stats_div.find_all("p")
    for p in paragraphs:
        if ":" in p.text:
            key, val = p.text.split(":", 1)
            data_bu[key.strip()] = val.strip()

with open("bu_facts_stats.json", "w", encoding="utf-8") as f:
    json.dump(data_bu, f, ensure_ascii=False, indent=4)

print("Boston University facts saved in bu_facts_stats.json")


# 2-)

url_uci = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url_uci)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"border": "1"})

datasets = []

if table:
    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 7:
            dataset = {
                "Name": cols[0].text.strip(),
                "Data Types": cols[1].text.strip(),
                "Task": cols[2].text.strip(),
                "Attribute Types": cols[3].text.strip(),
                "Instances": cols[4].text.strip(),
                "Attributes": cols[5].text.strip(),
                "Year": cols[6].text.strip(),
            }
            datasets.append(dataset)

with open("uci_datasets.json", "w", encoding="utf-8") as f:
    json.dump(datasets, f, ensure_ascii=False, indent=4)

print("UCI datasets saved in uci_datasets.json")


# 3-)

url_presidents = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url_presidents)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="wikitable")

presidents = []

if table:
    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all(["td", "th"])
        if len(cols) >= 7:
            prez = {
                "No": cols[0].text.strip(),
                "President": cols[1].text.strip(),
                "Party": cols[2].text.strip(),
                "Term of office": cols[3].text.strip(),
                "Election year": cols[4].text.strip(),
                "Vice President": cols[5].text.strip(),
                "Other info": cols[6].text.strip(),
            }
            presidents.append(prez)

with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, ensure_ascii=False, indent=4)

print("US presidents data saved in us_presidents.json")
