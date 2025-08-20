# Exercice jour 19

import json
import re
from collections import Counter


# Exercice Level 1


# 1-)
def count_lines_words(filename):

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count


filename = "./data/obama_speech.txt"
lines, words = count_lines_words(filename)
print(f"Fichier : {filename}")
print(f"Nombre de lignes : {lines}")
print(f"Nombre de mots : {words}")

files = [
    "./data/michelle_obama_speech.txt",
    "./data/donald_speech.txt",
    "./data/melina_trump_speech.txt",
]

for file in files:
    lines, words = count_lines_words(file)
    print(f"{file} -> Lignes : {lines}, Mots : {words}")


# 2-)
def most_spoken_languages(filename, n):

    with open(filename, "r", encoding="utf-8") as f:
        countries = json.load(f)

    language_counter = Counter()
    for country in countries:
        languages = country.get("languages", [])
        for lang in languages:
            language_counter[lang] += 1

    most_common = language_counter.most_common(n)
    return [(count, lang) for lang, count in most_common]


print(most_spoken_languages("./data/countries_data.json", 10))
print(most_spoken_languages("./data/countries_data.json", 3))

# 3-)


def most_populated_countries(filename, n):

    with open(filename, "r", encoding="utf-8") as f:
        countries = json.load(f)

    sorted_countries = sorted(
        countries, key=lambda c: c.get("population", 0), reverse=True
    )

    result = [
        {"country": c["name"], "population": c["population"]}
        for c in sorted_countries[:n]
    ]

    return result


print(most_populated_countries("./data/countries_data.json", 10))
print(most_populated_countries("./data/countries_data.json", 3))


# Exercice Level 2


# 4-)
def extract_emails(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return emails


emails = extract_emails("./data/email_exchange_big.txt")
print(emails)


# 5-)
def find_most_common_words(filename, top_n):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    words = re.findall(r"\b[a-z]+\b", text)
    counter = Counter(words)
    most_common = counter.most_common(top_n)
    return [(count, word) for word, count in most_common]


print(find_most_common_words("./data/sample.txt", 10))
print(find_most_common_words("./data/sample.txt", 5))
