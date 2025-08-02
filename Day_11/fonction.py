import math
from collections import Counter

            #Exercice Niveau 1

#1-)
def add_two_numbers(a, b):
    return a + b

#2-)
def area_of_circle(r):
    return math.pi * r * r

#3-)
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All elements must be numbers."

#4-)
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

#5-)
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    return 'Invalid month'

#6-)
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x2 != x1 else None

#7-)
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2

#8-)
def print_list(list):
    for item in list:
        print(item)

#9-)
def reverse_list(list):
    reversed_list = []
    for item in list[::-1]:
        reversed_list.append(item)
    return reversed_list

#10-)
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

#11-)
def add_item(lst, item):
    lst.append(item)
    return lst

#12-)
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

#13-)
def sum_of_numbers(n):
    return sum(range(n + 1))

#14-)
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

#15-)
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)



        # Exercice Niveau 2

#1-)
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of evens are {evens}. The number of odds are {odds}."

#2-)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#3-)
def is_empty(val):
    return not bool(val)

#4-)
def calculate_mean(list):
    return sum(list) / len(list)

def calculate_median(lst):
    list.sort()
    mid = len(list) // 2
    return (list[mid] + list[-mid-1]) / 2 if len(list) % 2 == 0 else list[mid]

def calculate_mode(list):
    return Counter(list).most_common(1)[0][0]

def calculate_range(list):
    return max(list) - min(list)

def calculate_variance(list):
    mean = calculate_mean(list)
    return sum((x - mean) ** 2 for x in list) / len(list)

def calculate_std(list):
    return math.sqrt(calculate_variance(list))

                #Exercice Niveau 3

#1-)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#2-)
def all_unique(lst):
    return len(lst) == len(set(lst))

#3-)
def same_data_type(lst):
    return all(isinstance(i, type(lst[0])) for i in lst)

#4-)
def is_valid_variable(name):
    return name.isidentifier()

#5-)
def most_spoken_languages(countries_data, top_n=10):
    lang_counter = Counter()
    for country in countries_data:
        lang_counter.update(country['languages'])
    return lang_counter.most_common(top_n)

def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]
