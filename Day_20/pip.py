import requests
import re
from collections import Counter
import numpy as np
import statistics
import pandas as pd

# 1. Read the Romeo and Juliet text and find the 10 most frequent words
url_romeo = 'http://www.gutenberg.org/files/1112/1112.txt'
response_romeo = requests.get(url_romeo)
text_romeo = response_romeo.text

words = re.findall(r'\b\w+\b', text_romeo.lower())
word_counts = Counter(words)
most_common_10_words = word_counts.most_common(10)
print("10 most frequent words in Romeo and Juliet:")
print(most_common_10_words)

# 2. Read the cats API and perform statistics and frequency analysis
cats_api = 'https://api.thecatapi.com/v1/breeds'
response_cats = requests.get(cats_api)
cats_data = response_cats.json()

weights_metric = []
lifespans_years = []
countries = []
breeds = []

for cat in cats_data:
    weight_metric_str = cat.get('weight', {}).get('metric', '')
    if weight_metric_str:
        try:
            w_min, w_max = weight_metric_str.split(' - ')
            w_min, w_max = float(w_min), float(w_max)
            weight_avg = (w_min + w_max) / 2
            weights_metric.append(weight_avg)
        except Exception:
            pass
    lifespan_str = cat.get('life_span', '')
    if lifespan_str:
        try:
            ls_min, ls_max = lifespan_str.split(' - ')
            ls_min, ls_max = float(ls_min), float(ls_max)
            lifespan_avg = (ls_min + ls_max) / 2
            lifespans_years.append(lifespan_avg)
        except Exception:
            pass
    origin = cat.get('origin', '')
    breed = cat.get('name', '')
    if origin:
        countries.append(origin)
    if breed:
        breeds.append(breed)

weight_stats = {
    'min': np.min(weights_metric),
    'max': np.max(weights_metric),
    'mean': np.mean(weights_metric),
    'median': np.median(weights_metric),
    'std_dev': np.std(weights_metric)
}

lifespan_stats = {
    'min': np.min(lifespans_years),
    'max': np.max(lifespans_years),
    'mean': np.mean(lifespans_years),
    'median': np.median(lifespans_years),
    'std_dev': np.std(lifespans_years)
}

country_counts = Counter(countries)
breed_counts = Counter(breeds)

print("\nCats' weight statistics in metric units (kg):")
print(weight_stats)
print("\nCats' lifespan statistics (years):")
print(lifespan_stats)
print("\nFrequency table of cats' countries of origin:")
print(country_counts.most_common())
print("\nFrequency table of cat breeds:")
print(breed_counts.most_common())

# 3. Read the countries API to find largest countries and languages info
countries_api_url = 'https://restcountries.com/v3.1/all'
response_countries = requests.get(countries_api_url)
countries_data = response_countries.json()

country_areas = []
language_counts = Counter()
country_languages_set = set()

for c in countries_data:
    try:
        area = c.get('area', 0)
        country_name = c['name']['common']
        country_areas.append((country_name, area))
        langs = c.get('languages', {})
        for lang_name in langs.values():
            language_counts[lang_name] += 1
            country_languages_set.add(lang_name)
    except:
        pass

country_areas_sorted = sorted(country_areas, key=lambda x: x[1], reverse=True)
largest_10_countries = country_areas_sorted[:10]
top_10_languages = language_counts.most_common(10)
total_languages = len(country_languages_set)

print("\n10 largest countries by area:")
for country, area in largest_10_countries:
    print(f"{country}: {area} km²")

print("\n10 most spoken languages by number of countries using them as official language:")
for lang, count in top_10_languages:
    print(f"{lang}: {count} countries")

print(f"\nTotal number of languages in the countries API: {total_languages}")

# 4. Read the UCI datasets webpage content (only preview without parsing)
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
uci_response = requests.get(uci_url)
uci_content_preview = uci_response.text[:500]  # Only preview text to confirm access
print("\nPreview of UCI datasets webpage content:")
print(uci_content_preview)
