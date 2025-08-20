# Exercice Jour 13

# 1-)
nbres = [-4, -3, -2, -1, 0, 2, 4, 6]
nbres_neg_et_zero = [n for n in nbres if n <= 0]
print(nbres_neg_et_zero)

# 2-)
list_de_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplatie = [n for sublist in list_de_lists for inner in sublist for n in inner]
print(aplatie)

# 3-)
resultat = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
for ligne in resultat:
    print(ligne)

# 4-)
pays = [[("Finlande", "Helsinki")], [("Suède", "Stockholm")], [("Norvège", "Oslo")]]
codes = ["Fin", "Swe", "Nor"]
nouvelle_liste = [[p[0], code, p[1]] for ([p], code) in zip(pays, codes)]
print(nouvelle_liste)

# 5-)
pays = [[("Finlande", "Helsinki")], [("Suède", "Stockholm")], [("Norvège", "Oslo")]]
dictionnaires = [{"country": p[0][0], "City": p[0][1]} for p in pays]
print(dictionnaires)

# 6-)
Noms = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
concaténée = [" ".join(name) for sublist in Noms for name in sublist]
print(concaténée)

# 7-)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
print(slope(2, 3, 5, 11))  # ➜ 2.666...
