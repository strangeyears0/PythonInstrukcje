#PROSTY SŁOWNIK


# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

#UZYSKIWANIE DOSTĘPU DO WARTOŚCI SŁOWNIKA

# alien_0 = {'color': 'zielony', 'points': 5}
# new_points = alien_0['points']
#
# print("Zdobyłeś "+ str(new_points) + " punktów")
#
#
#DODANIE NOWEJ PARY KLUCZ WARTOŚĆ
#
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#
# print(alien_0)

# ROZPOCZĘCIE PRACY OD PUSTEGO SŁOWNIKA
#
# alien_0 = {}
# alien_0['color'] = 'zielony'
# alien_0['points'] = 5
#
# print(alien_0)
#

# MODYFIKOWANIE WARTOŚCI SŁOWNIKA

# alien_0 = {'color': 'zielony'}
# print(f"Obcy ma kolor {alien_0['color']}.")
#
# alien_0['color'] = 'żółty jak papiesz'
# print(f"Obcy ma teraz kolor {alien_0['color']}.")

#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'średnio'}
# print("Początkowa wartość x-position: " + str(alien_0['x_position']))
#
# if alien_0['speed'] == 'wolno':
#     x_increment = 1
# elif alien_0['speed'] == 'średnio':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position']+x_increment
#
# print("Nowa wartość x-position: "+ str(alien_0['x_position']))

#USUWANIE PARY KLUCZ-WARTOŚĆ
#
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

#SŁOWNIK PODOBNYCH OBIEKTÓW

# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
#
# print(f"Ulubiony język programowania Papiesza to {fav_lang['papiesz'].title()}")


#6.1
#
# person = {
#     'name':'Papiesz',
#     'surname':'Święty',
#     'age': 2137,
#     'city': 'Polska'
# }
#
# print(f"{person}")

#6.2
#
# fav_numbers= {
#     'anna':9,
#     'juzef':1,
#     'mati':3,
#     'dawid':4,
#     'jolanta':5
#
# }
# print((f"{fav_numbers}"))

#6.3

# glosariusz={
#     'print':'\ndrukuj',
#     'if': '\njeżeli',
#     'while': '\ndopóki',
#     'and': '\ni',
#     'true': '\nprawda'
# }
# print(f"Print oznacza: {glosariusz['print'].title()}")
# print(f"If oznacza:{glosariusz['if'].title()} ")
# print(f"While oznacza:{glosariusz['while'].title()} ")
# print(f"And oznacza:{glosariusz['and'].title()} ")
# print(f"True oznacza:{glosariusz['true'].title()} ")