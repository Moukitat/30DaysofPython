# Exercice: Jour 8

# 1
chien = {}

# 2
chien = {"nom": "Namir", "couleur": "Blanc", "race": "Labrador", "jambes": 4, "âge": 4}

# 3
etudiant = {
    "prenom": "miss",
    "nom": "INDIENNE",
    "sexe": "Feminin",
    "âge": 19,
    "statut_matrimonial": "célibataire",
    "competences": ["Python", "Analyse de données"],
    "pays": "Togo",
    "ville": "Lomé",
    "adresse": "avedji",
}

# 4
print(len(etudiant))

# 5
competences = etudiant["competences"]
print(competences)
print(type(competences))

# 6
etudiant["competences"].append("Cloud computing")
etudiant["competences"].append("AI")
print(etudiant["competences"])

# 7
cles = list(etudiant.keys())
print(cles)

# 8
valeurs = list(etudiant.values())
print(valeurs)

# 9
items = list(etudiant.items())
print(items)

# 10
del etudiant["statut_matrimonial"]
print(etudiant)

# 11
del chien
