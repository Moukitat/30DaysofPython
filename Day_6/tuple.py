#Exercice Niveau 1

#1-)
empty_tuple = ()

#2-)
brothers = ('Abdoul', 'Wasiu')
sisters = ('Amira', 'Moukitat')

#3-)
siblings = brothers + sisters
print(siblings)  

#4-)
print("Combien de frères et sœurs avez vous ?:", len(siblings))  

#5-)
family_members = siblings + ('Papa', 'Maman')
print(family_members)  


#Exercice Niveau 2

#1-)
freres_soeurs, papa, maman = family_members
print("les frères et les sœurs :", freres_soeurs)
print("papa :", papa)
print("Maman :", maman)

#2-)
fruits = ('pomme', 'fraise', 'orange')
legumes = ('carotte', 'tomate', 'obergine')
animal_products = ('lait', 'fromage', 'œuf')

food_stuff_tp = fruits + legumes + animal_products
print(food_stuff_tp)

#3-)
Food_Stuff_LT = list(food_stuff_tp)

#4-)
middle_index = len(Food_Stuff_LT) // 2
if len(Food_Stuff_LT) % 2 == 0:
    print("L'éléments du milieu :", Food_Stuff_LT[middle_index-1:middle_index+1])
else:
    print("L'élément du milieu :", Food_Stuff_LT[middle_index])

#5-)
print("Les 3 premiers :", Food_Stuff_LT[:3])
print("Les 3 derniers :", Food_Stuff_LT[-3:])

#6-)
del food_stuff_tp

#7-)
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonie' in nordic_countries)  
print('Iceland' in nordic_countries)  
