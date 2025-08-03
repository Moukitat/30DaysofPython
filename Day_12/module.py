#Exercice Jour 12
                        #Exercice Niveau 1

#1
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

print(random_user_id())

#2
def user_id_gen_by_user():
    nb_caracteres = int(input("Entrez le nombre de caractères par ID : "))
    nb_ids = int(input("Entrez le nombre d'ID à générer : "))
    
    caracteres = string.ascii_letters + string.digits
    for _ in range(nb_ids):
        user_id = ''.join(random.choices(caracteres, k=nb_caracteres))
        print(user_id)
user_id_gen_by_user()

#3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

                            #Exercice Niveau 2
#1-)
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors

print(list_of_hexa_colors(3))

#2-)
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print(list_of_rgb_colors(3))

#3-)
def generate_colors(format, n):
    if format == 'hexa':
        return list_of_hexa_colors(n)
    elif format == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Format inconnu. Utilisez 'hexa' ou 'rgb'."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))


                            #Exercice Niveau 3
#1-)
def shuffle_list(liste):
    random.shuffle(liste)
    return liste

print(shuffle_list([22, 8, 25, 23, 25]))

#2-)
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())


