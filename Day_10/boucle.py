# Exercice : jour 10
# Niveau1

# 1-) Boucle for de 0 à 10
for i in range(11):
    print(i)

# Boucle while de 0 à 10
i = 0
while i <= 10:
    print(i)
    i += 1

# 2-) Boucle for de 10 à 0
for i in range(10, -1, -1):
    print(i)

# Boucle while de 10 à 0
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3-) Triangle avec print()
for i in range(1, 8):
    print("#" * i)

# 4-) Grille de dièses (boucles imbriquées)
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

# 5-) Afficher le carré des nombres
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6-) Itérer sur une liste
technos = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for tech in technos:
    print(tech)

# 7-) Afficher les nombres pairs de 0 à 100
for i in range(101):
    if i % 2 == 0:
        print(i)

# 8-) Afficher les nombres impairs de 0 à 100
for i in range(101):
    if i % 2 != 0:
        print(i)

        # Exercice Niveau 2

# 1-) Somme de tous les nombres de 0 à 100
total = 0
for i in range(101):
    total += i
print("La somme de tous les nombres est:", total)

# 2-) Somme des pairs et impairs
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("La somme des nombres pairs est:", sum_even)
print("La somme des nombres impairs est:", sum_odd)


# Exercice Niveau 3

from countries import countries

# les pays
for country in countries:
    if "land" in country:
        print(country)

        # la liste des fruits
fruits = ["banana", "orange", "mango", "lemon"]
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)


# le nombre total des langues
from countries import countries
from countries import countries

# Nombre total de langues
languages = set()
for country in countries:
    for lang in country["languages"]:
        languages.add(lang)
print("Nombre total de langues:", len(languages))

# 10 langues les plus parlées
from collections import Counter

lang_counter = Counter()
for country in countries:
    lang_counter.update(country["languages"])

most_spoken = lang_counter.most_common(10)
print("Top 10 des langues les plus parlées:")
for lang, count in most_spoken:
    print(f"{lang}: {count}")

# 10 pays les plus peuplés
most_populated = sorted(countries, key=lambda x: x["population"], reverse=True)[:10]
print("Top 10 des pays les plus peuplés:")
for country in most_populated:
    print(f"{country['name']}: {country['population']}")
