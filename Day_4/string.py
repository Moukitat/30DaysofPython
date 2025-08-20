# 1–)
phrase1 = " ".join(["trente", "jours", "de", "python"])

# 2-)
phrase2 = " ".join(["codage", "pour", "tous"])

# 3
societe = "codage pour tous"

# 4
print(societe)

# 5
print(len(societe))

# 6
print(societe.upper())

# 7
print(societe.lower())

# 8
chaine = "Coding For All"
print(chaine.capitalize())
print(chaine.title())
print(chaine.swapcase())

# 9
phrase = "Coding For All"
resultat = " ".join(phrase.split()[1:])
print(resultat)

# 10
print("codage" in "Coding For All")

# 11
société = "codage pour tous"
print(société.replace("codage", "Python"))

# 12-)
texte = "Python pour tout le monde"
print(texte.replace("tout le monde", "tous"))

# 13-)
société = "codage pour tous"
print(société.split())

# 14-)
entreprises = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(entreprises.split(", "))

# 15-)
text = "Coding For All"
print(text[0])

# 16-)
print(len("Coding For All") - 1)

# 17-)
text = "codage pour toutes"
print(text[10])


# 18-)
phrase = "Python pour tout le monde"
acronyme = "".join(word[0].upper() for word in phrase.split())
print(acronyme)

# 19-)
phrase = "codage pour tous"
acronyme = "".join(word[0].upper() for word in phrase.split())
print(acronyme)

# 20-)
text = "codage pour tous"
print(text.find("C"))
# 21-)
text = "Coding For All"
print(text.find("F"))

# 22-)
text = "Coding For All"
print(text.rfind("l"))

# 23-)
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
print(phrase.find("parce que"))

# 24-)
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
print(phrase.rindex("parce que"))

# 25-)
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que parce que c'est une conjonction"
print(phrase[44:69])

# 26-)
print(phrase.find("parce que"))

# 27-)
print(phrase[44:69])

# 28-)
text = "Coding For All"
print(text.startswith("Coding"))

# 29-)
text = "Coding For All"
print(text.endswith("coding"))

# 30-)
text = "  codage pour tous  "
print(text.strip())

# 31-)
print("30daysofpython".isidentifier())
print("Thirty_days_of_python".isidentifier())

# 32-)
libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" # ".join(libs))

# 33-)
print("J'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape.")

# 34-)
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35-)
radius = 10
area = 3.14 * radius**2
print(
    "La zone d'un cercle avec le rayon {} est de {:.0f} mètres carrés.".format(
        radius, area
    )
)

# 36-)
x, y = 8, 6
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")
print(f"{x} % {y} = {x % y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} ** {y} = {x ** y}")
