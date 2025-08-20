# Exercice Niveau 2

# 1-) la version de Python que j'utilise
Python: 3.11

# 2-)les opérations

x = 3
y = 4

print("Addition:", x + y)
print("Soustraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulo:", x % y)
print("Exponentielle:", x**y)
print("Floor Division:", x // y)

# 3-)les chaines sur la coque interactive Python


Prenom = "Moukitat"
Nom = "LASSISI"
pays = "Togo"
objectif = "Je profite de 30 jours de Python"

print(Prenom)
print(Nom)
print(pays)
print(objectif)


# 4-)vérification des types de données de ces données suivantes

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finlande"]))
print(type("Moukitat"))
print(type("LASSISI"))
print(type("Togo"))


# Exercice: Niveau 3

# 1-) Exemple pour différents types de dànnées Python


entier = 42

float = 3.14

complexe = 2 + 3j

String = "Bonjour, Python !"

bool = True

liste = [22, "Python", True]

tuple = (22, "tuple")

set = {1, 2, 3, 3, 4}

dict = {"Nom": "LASSISI", "Prénom": "Moukitat", "âge": "20"}

print(type(entier), entier)
print(type(float), float)
print(type(complexe), complexe)
print(type(String), String)
print(type(bool), bool)
print(type(liste), liste)
print(type(tuple), tuple)
print(type(set), set)
print(type(dict), dict)


# 2-)La distance euclidienne entre (2, 3) et (10, 8)

import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance euclidienne :", distance)
