                #Exercice Niveau 1

#1-)
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#2-)
it_companies.add('Twitter')
print(it_companies)

#3-)
it_companies.update(['digijob', 'Lync-Informatique', 'Tiktok'])
print(it_companies)

#4-)
it_companies.remove('IBM')
print(it_companies)

#5-)
- supprimer lève une erreur si l’élément n’existe pas dans l’ensemble.

- rejeter ne lève pas d’erreur si l’élément n’existe pas.



            #Exercice Niveau 2

#1-)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))

#2-)
print(A.intersection(B))

#3-)
print(A.issubset(B))

#4-)
print(A.isdisjoint(B))

#5-)
print(A.union(B))
print(B.union(A))  

#6-)
print(A.symmetric_difference(B))

#7-)
A.clear()
B.clear()
print(A, B)



            #Exercice Niveau 3
#1-)
age_list = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age_list)

print("Taille de la liste :", len(age_list))
print("Taille de l'ensemble :", len(age_set))

#2-) La différence entre les types de données

- Une chaîne: est une séquence de caractères. Elle est utilisée pour représenter du texte.
- Une liste: est une collection ordonnée et modifiable (mutable).
- Un tuple: est comme une liste, mais immuable.
- Un ensemble: est une collection non ordonnée d’éléments uniques.

#3-)
text = "I am a teacher and I love to inspire and teach people"
words = text.split()
unique_words = set(words)
print("Le nombre de mots uniques est:", len(unique_words))
