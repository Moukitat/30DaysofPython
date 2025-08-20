# Exercice Niveau 1

# 1-)
ma_liste = []

# 2-)
gammes = ["pc", "battérie", "disque", "souris", "clé", "chargeur"]

# 3-)
print(len(gammes))


# 4-)
print(gammes[0])
print(gammes[len(gammes) // 2])
print(gammes[-1])


# 5-)
mixtes_data_types = ["Moukitat", 19, 1.62, "Promis", "Lomé"]

# 6-)
IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7-)
print(IT_COMPANIES)

# 8-)
print(len(IT_COMPANIES))

# 9-)
print(IT_COMPANIES[0])
print(IT_COMPANIES[len(IT_COMPANIES) // 2])
print(IT_COMPANIES[-1])

# 10-)
IT_COMPANIES[1] = "Meta"
print(IT_COMPANIES)

# 11-)
IT_COMPANIES.append("Lync-Informatique")
print(IT_COMPANIES)


# 12-)
IT_COMPANIES.insert(len(IT_COMPANIES) // 2, "digijob")
print(IT_COMPANIES)

# 13-)
for i in range(len(IT_COMPANIES)):
    if IT_COMPANIES[i] != "IBM":
        IT_COMPANIES[i] = "Up It"
        break
print(IT_COMPANIES)

# 14-)
IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# vérifions si Facebook existe
if "Facebook" in IT_COMPANIES:
    print("Facebook existe dans la liste.")
else:
    print("Facebook n'existe pas dans la liste.")

# 16-)
IT_COMPANIES.sort()
print(IT_COMPANIES)

# 17-)
IT_COMPANIES.reverse()
print(IT_COMPANIES)

# 18-)
del IT_COMPANIES[:3]
print(IT_COMPANIES)

# 19-)
del IT_COMPANIES[-3:]
print(IT_COMPANIES)

# 20-)
milieu = IT_COMPANIES[len(IT_COMPANIES) // 2 : len(IT_COMPANIES) // 2 + 1]
print(milieu)

# 21-)
IT_COMPANIES.pop()
print(IT_COMPANIES)

# 22-)
front_end = ["html", "css", "js", "react", "redux"]
back_end = ["node", "express", "mongodb"]
full_stack = front_end + back_end

# 23-)
index_redux = full_stack.index("redux")
full_stack.insert(index_redux + 1, "Python")
full_stack.insert(index_redux + 2, "SQL")
print(full_stack)


# Exercice Niveau 2

# 1-)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Trié:", ages)
print("Min:", min(ages))
print("Max:", max(ages))

# Ajout
ages.extend([min(ages), max(ages)])
print("Avec min et max:", ages)

# Médiane
ages.sort()
n = len(ages)
median = (ages[n // 2] + ages[n // 2 - 1]) / 2 if n % 2 == 0 else ages[n // 2]
print("Médiane:", median)

# Moyenne
average = sum(ages) / len(ages)
print("Moyenne:", average)

# Écart
print("Écart abs(min - moyenne):", abs(min(ages) - average))
print("Écart abs(max - moyenne):", abs(max(ages) - average))

# 2-)
countries = [
    "Chine",
    "Russie",
    "États-Unis",
    "Finlande",
    "Suède",
    "Norvège",
    "Danemark",
]
milieu = countries[len(countries) // 2]
print("Pays du milieu:", milieu)

n = len(countries)
if n % 2 == 0:
    moitié1 = countries[: n // 2]
    moitié2 = countries[n // 2 :]
else:
    moitié1 = countries[: n // 2 + 1]
    moitié2 = countries[n // 2 + 1 :]

print("Première moitié:", moitié1)
print("Deuxième moitié:", moitié2)

# 3-)
nordiques = countries[3:]
autres = countries[:3]
print("Pays nordiques:", nordiques)
print("Autres pays:", autres)
