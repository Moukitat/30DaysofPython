
# Exercices Jour3

#1-)
age = 19

#2-)
taille = 1.75

#3-)
nombre_complexe = 8 + 22j

#4-)
base = float(input("Veuillez saisir la base du triangle: "))
hauteur = float(input("Veuillez saisir la hauteur du triangle: "))
zone_triangle = 0.5 * base * hauteur
print("La zone du triangle est:", zone_triangle)

#5-)
a = float(input("Entrez le côté A: "))
b = float(input("Entrez le côté B: "))
c = float(input("Entrez le côté C: "))
perimetre_triangle = a + b + c
print("Le périmètre du triangle est:", perimetre_triangle)

#6-)
longueur = float(input("Veuillez saisir la longueur du rectangle: "))
largeur = float(input("Veuillez saisir la largeur du rectangle: "))
surface_rectangle = longueur * largeur
perimetre_rectangle = (longueur + largeur) * 2
print("La surface est:", surface_rectangle)
print("Le périmètre est:", perimetre_rectangle)

#7-)
rayon = float(input("Veuillez saisir le rayon du cercle: "))
pi = 3.14
zone_cercle = pi * rayon ** 2
circonference = 2 * pi * rayon
print("L'aire du cercle est:", zone_cercle)
print("La circonférence est:", circonference)

#8-)
x = 3
y = 2 * x - 2
print("Pour x =", x, ", y =", y)

# 9. Pente et distance euclidienne entre (2, 2) et (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pente = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La pente est:", pente)
print("La distance euclidienne est:", distance)

#10-)
print("Les pentes sont égales :", pente == 2)

#11-)
for x in range(-10, 4):
    y = x**2 + 6*x + 9
    if y == 0:
        print("x où y=0 est :", x)

#12-)
print(len("Python") != len("Dragon"))

#13-)
print('on' in "python" and 'on' in "dragon")

#-14-)
phrase = "I hope this course is not full of jargon."
print("jargon" in phrase)

#15-)
print('on' not in "Python" and 'on' not in "Dragon")

#16-)
texte = "python"
longueur = len(texte)
print(float(longueur))
print(str(longueur))

#17-)
nombre = int(input("Veuillez saisir un nombre: "))
print(nombre % 2 == 0)

#18-)
print(7 // 3 == int(2.7))  # True

#19-)
print(type("10") == type(10))  # False

#20-)
try:
    print(int('9.8') == 10)
except ValueError:
    print("Erreur: '9.8' n'est pas un int")

#21-)
heures = float(input("Entrez des heures: "))
pourcentage = float(input("Entrez le pourcentage par heure: "))
remuneration = heures * pourcentage
print("Votre gain hebdomadaire est de", remuneration)

#22-)
annees = int(input("Entrez le nombre d'années que vous avez vécu: "))
secondes = annees * 365 * 24 * 60 * 60
print("Vous vivez pendant", secondes, "secondes")

#23-)
l1 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 4]
l2 = [8, 3, 1, 3, 9, 27, 4, 1, 4, 1]
l3 = [6, 64, 5, 1, 5, 25, 125]
print(*l1, sep=' ')
print(*l2, sep=' ')
print(*l3, sep=' ')
