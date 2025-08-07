from datetime import datetime, timedelta

#1-)
now = datetime.now()

current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print(f"Jour : {current_day}")
print(f"Mois : {current_month}")
print(f"Année : {current_year}")
print(f"Heure : {current_hour}")
print(f"Minute : {current_minute}")
print(f"Horodatage (timestamp) : {current_timestamp}")

#2-)
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

#3-)
time_string = "5 December, 2019"
time_obj = datetime.strptime(time_string, "%d %B, %Y")
print(time_obj)

#4-)
new_year = datetime(current_year + 1, 1, 1)
time_diff_new_year = new_year - now

days = time_diff_new_year.days
hours = time_diff_new_year.seconds // 3600
minutes = (time_diff_new_year.seconds % 3600) // 60
seconds = time_diff_new_year.seconds % 60

print(f"Temps restant jusqu'à la nouvelle année : {days} jours, {hours} heures, {minutes} minutes, {seconds} secondes")

#5-)
epoch = datetime(1970, 1, 1)
time_diff_epoch = now - epoch
print(f"Temps écoulé depuis le 1er janvier 1970 : {time_diff_new_year.days} jours et {time_diff_new_year.seconds} secondes")

#6-)
-Gestion et manipulation des dates et heures
-Analyse des séries chronologiques
-Horodatage des événements
-Planification et rappels
-Gestion des fuseaux horaires
-Calculs de durées et d’âges
-Organisation de contenu chronologique