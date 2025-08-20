# Exercice jour 14


# Niveau 1
# 3
def carré(x):
    return x**2


nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = list(map(carré, nombres))
print(resultat)

# 4
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
for pays in countries:
    print(pays)

# 5
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
for nom in names:
    print(nom)

# 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nombre in numbers:
    print(nombre)

    # Niveau 2

# 1
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
majuscule_countries = list(map(str.upper, countries))
print(majuscule_countries)

# 2
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carres = list(map(lambda x: x**2, nombres))
print(carres)

# 3
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
majuscule_names = list(map(str.upper, names))
print(majuscule_names)

# 4
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
pays_land = list(filter(lambda c: "land" in c, countries))
print(pays_land)

# 5
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
pays_6_chars = list(filter(lambda c: len(c) == 6, countries))
print(pays_6_chars)

# 6
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
pays_6_plus = list(filter(lambda c: len(c) >= 6, countries))
print(pays_6_plus)

# 7
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
pays_e = list(filter(lambda c: c.startswith("E"), countries))
print(pays_e)

# 8
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
resultat = reduce(
    lambda acc, c: acc + c + ", ",
    filter(lambda c: "LAND" in c, map(str.upper, countries)),
    "",
)

resultat = resultat.rstrip(", ") + " sont des pays nord-européens."
print(resultat)


# 9
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]


mixte = ["Asabeneh", 42, "Lidiya", True, "Ermias", 3.14]
strings_only = get_string_lists(mixte)
print(strings_only)


# 10-)
from functools import reduce

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somme = reduce(lambda acc, x: acc + x, nombres)
print(somme)

# 11-)
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
phrase = (
    reduce(
        lambda acc, c: acc + ", " + c if c != countries[-1] else acc + " et " + c,
        countries[:-1],
        "",
    )
    + " sont des pays nord-européens."
)
phrase = phrase.lstrip(", ")
print(phrase)

# 12-)
from countries import countries


def categorize_countries(countries):
    patterns = ["land", "ia", "island", "stan"]
    resultat = []
    for pattern in patterns:
        pays_avec_pattern = [c for c in countries if pattern in c.lower()]
        resultat.extend(pays_avec_pattern)
    return list(set(resultat))


filtrés = categorize_countries(countries)
print(filtrés)


# 13-)
def count_countries_by_initial(countries):
    compteur = {}
    for pays in countries:
        initiale = pays[0].upper()
        compteur[initiale] = compteur.get(initiale, 0) + 1
    return compteur


countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
resultat = count_countries_by_initial(countries)
print(resultat)

# 14-)
from countries import countries


def get_first_ten_countries(countries):
    return countries[:10]


premiers_dix = get_first_ten_countries(countries)
print(premiers_dix)


# 15-)
from countries import countries


def get_last_ten_countries(countries):
    return countries[-10:]


derniers_dix = get_last_ten_countries(countries)
print(derniers_dix)


# Niveau 3

# 1
from countries_data import countries_data

# Trier par nom
tri_nom = sorted(countries_data, key=lambda c: c["name"])
print(tri_nom)

# Trier par capitale
from countries_data import countries_data

tri_capitale = sorted(countries_data, key=lambda c: c.get("capital", ""))
print(tri_capitale)

# Trier par population décroissante
from countries_data import countries_data

tri_population = sorted(countries_data, key=lambda c: c["population"], reverse=True)
print(tri_population)

# Trouver les 10 langues les plus parlées (en comptant occurrences dans countries_data)
from collections import Counter
from countries_data import countries_data

langues = Counter()
for country in countries_data:
    langues.update(country.get("languages", []))
    print(langues)
top_10_langues = langues.most_common(10)


# Les 10 pays les plus peuplés (déjà dans tri_population)
from collections import Counter
from countries_data import countries_data

tri_population = sorted(countries_data, key=lambda c: c["population"], reverse=True)
top_10_pays_peuples = tri_population[:10]
print(top_10_pays_peuples)
