#Jour 2: 30 Days of Python Programming

#Exercice niveau 1

Prénom = "Moukitat"
Nom = "LASSISI"
Nom_complet = "Moukitat LASSIS"
Pays = "Togo"
Ville = "Lomé"
an = 2025
âge = 20
est_Married = False
is_true = True
IS_light_on = "Yes"
M, L, W, B = 1, 2, 3, 4


#Exercice niveau 2

#1 les types des variables
print(type(Prénom))
print(type(Nom))
print(type(Nom_complet))
print(type(Pays))
print(type(Ville))
print(type(an))
print(type(âge))
print(type(est_Married))
print(type(is_true))
print(type(IS_light_on))
print(type(M))

#2
print(len(Prénom))

#3
print(len(Prénom)>len(Nom))

#4
num_one = 5
num_two = 4

#5 addition
som = num_one + num_two
print(som)

#6 soustration
soustr = num_one - num_two
print(soustr)

#7 multiplication
prod = num_one * num_two
print(prod)

#8 division
div = num_one / num_two
print(div)

#9 modulo
mod = num_two % num_one
print(mod)

#10 floor_division
floor_division = num_one // num_two
print(floor_division)

#12
rayon = 30
pi = 3.1416

# i
area_of_circle = pi * rayon ** 2

# ii
circum_of_circle = 2 * pi * rayon

# iii
rayon_user = float(input("Entrez le rayon du cercle : "))
area_user = pi * rayon_user ** 2
print(area_user)

#13
user_Prénom = input("Entrez votre prénom : ")
user_Nom = input("Entrez votre nom : ")
user_Pays = input("Entrez votre pays : ")
user_âge = int(input("Entrez votre âge : "))

#14 (voir ficher shell.py)
help("keywords")
