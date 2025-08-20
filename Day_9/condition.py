# Exercice jour9: Niveau1

# 1-)
age = int(input("Entrez votre âge: "))
if age >= 18:
    print("Vous êtes assez vieux pour apprendre à conduire.")
else:
    print(f"Vous avez besoin de {18 - age} ans de plus pour apprendre à conduire.")

# 2-)
my_age = 19
your_age = int(input("Entrez votre âge: "))
diff = abs(my_age - your_age)

if your_age > my_age:
    print(f"Vous avez {diff} {'an' if diff == 1 else 'ans'} de plus que moi.")
elif your_age < my_age:
    print(f"Je suis plus âgé que vous de {diff} {'an' if diff == 1 else 'ans'}.")
else:
    print("Nous avons le même âge.")

# 3-)
x = int(input("Entrez un premier nombre: "))
y = int(input("Entrez un second nombre: "))

if x > y:
    print(f"{x} est supérieur à {y}")
elif x < y:
    print(f"{x} est inférieur à {y}")
else:
    print(f"{x} est égal à {y}")

    # Niveau 2

# 1-)
note = int(input("Entrez votre note: "))

if 80 <= note <= 100:
    print("A")
elif 70 <= note <= 79:
    print("B")
elif 60 <= note <= 69:
    print("C")
elif 50 <= note <= 59:
    print("D")
else:
    print("F")


# 2-)
mois = input("Entrez un mois: ")
if mois in ["Septembre", "Octobre", "Novembre"]:
    print("Automne")
elif mois in ["Décembre", "Janvier", "Février"]:
    print("Hiver")
elif mois in ["Mars", "Avril", "Mai"]:
    print("Printemps")
elif mois in ["Juin", "Juillet", "Août"]:
    print("Été")
else:
    print("Mois invalide")


# 3-)
fruits = ["banana", "orange", "mango", "lemon"]
nouveau = input("Entrez un fruit: ").lower()

if nouveau in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(nouveau)
    print("Fruit ajouté. Nouvelle liste:", fruits)

    # Niveau 3
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "compétences": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

if "compétences" in person:
    compétences = person["compétences"]
    intermédiaire = compétences[len(compétences) // 2]
    print("Les compétences intermédiaires :", intermédiaire)

if "Python" in person.get("compétences", []):
    print("La personne a des compétences Python .")

compétences = person["compétences"]
if compétences == ["JavaScript", "React"]:
    print("Il est un développeur frontal")
elif all(y in compétences for y in ["Node", "Python", "MongoDB"]):
    print("Il est un développeur backend")
elif all(y in compétences for y in ["React", "Node", "MongoDB"]):
    print("Il est un développeur fullstack")
else:
    print("Titre inconnu")

if person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} vit en Finlande. Il est marié."
    )
