#LISTA SŁOWNIKÓW

# alien_0 = {'color':'zielony','points':5}
# alien_1 = {'color':'zolty','points':10}
# alien_2 = {'color':'czerwony','points':15}
#
# aliens = [alien_0,alien_1,alien_2]
#
# for alien in aliens:
#     print(alien)


# #Utworzenie pustej listy przeznaczonej do przechowywania obcych
# aliens = []
#
# #utworzenie 30 obcych
#
# for alien_number in range(30):
#     new_alien = {'color':'zielony','points':5,'speed':'wolno'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color']=='zielony':
#         alien['color']='żółty'
#         alien['speed']='średnio'
#         alien['points']=10
#     elif alien['color']=='żółty':
#         alien['color'] = 'czerwony'
#         alien['speed'] = 'szybko'
#         alien['points'] = 15
# #wyświetlanie pierwszych 5 obcych
# for alien in aliens[:5]:
#     print(alien)
# print('...')
#
# #wyświetlanie całkowitej liczby utworzonych obcych
# print(f"Całkowita liczba obcych {str(len(aliens))}")

#LISTA W SŁOWNIKU

#przechowywanie informajci o pizzy zamawianej przez klienta

# pizza = {
#     'crust':'grubym',
#     'toppings':['pieczarki','podwójny ser'],
# }
#
# #podsumowanie zamówienia
# print(f"Zamówiłeś pizza na {pizza['crust']} cieście wraz z następującymi dodatkami:")
# for topping in pizza['toppings']:
#     print(f"\t{topping.title()}")

# fav_lang = {
#     'janek':['python','ruby'],
#     'sara':['c'],
#     'edward':['ruby','go'],
#     'paweł':['python','haskell'],
#
# }
#
# for name,langs in fav_lang.items():
#     print(f"\nUlubione języki programowania użytkownika {name.title()} to:")
#     for lang in langs:
#         print(f"\t {lang.title()}")


#SŁOWNIK W SŁOWNIKU
# users = {
#     'aeinstein':{
#         'first':'albert',
#         'last':'einstein',
#         'location':'princeton',
#     },
#     'mcurie':{
#         'first': 'maria',
#         'last': 'sklodowska-curie',
#         'location': 'paryz',
#     },
# }
#
# for username,user_info in users.items():
#     print(f"\nNazwa użytkownika: {username}")
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#
#     print(f"\tImię i nazwisko: {full_name.title()}")
#     print(f"\tMiejscowość: {location.title()}")

#6.7


# person = {
#     'name':'Papiesz',
#     'surname':'Święty',
#     'age': 2137,
#     'city': 'Kraków'
# }
#
# person_2={
#     'name': 'Jerzy',
#     'surname': 'Sthut',
#     'age': 75,
#     'city': 'Warszawa'
# }
#
# person_3={
#     'name': 'Jan',
#     'surname': 'Urban',
#     'age': 90,
#     'city': 'Łódź'
# }
#
# people= [person,person_2,person_3]
#
# for person in people:
#     print(person)

#6.8

# elephant={
#     'name':'Elephtant Andrzej',
#     'from':'Africa',
#     'size':'big',
# }
# cat={
#     'name':'Cat Hera',
#     'from':'Europe',
#     'size':'small',
# }
# seal={
#     'name':'Seal Foka',
#     'from':'Grenland',
#     'size':'medium'
# }
#
# pets=[elephant,cat,seal]
# for pet in pets:
#     print(f"Mam na imię: {pet['name']}\n Jestem z: {pet['from']}\n Mój rozmiar to: {pet['size'].title()}")

#6.9
#
# favorite_places ={
#     'Andrzej':['Łódź','Warszawa','Kraków'],
#     'Beata':["Międzyzdroje",'Wieliczka','Bochnia'],
#     'Hera':["Kuweta","Drzewo",'Klatka']
#
# }
# for name,places in favorite_places.items():
#     print(f"Ulubione miejsce użytkownika: {name.title()}")
#     for place in places:
#         print(f"\n{place}")


#6.10

#
# fav_numbers= {
#     'anna':[9,1],
#     'juzef':[11,4],
#     'mati':[13,2],
#     'dawid':[54,65],
#     'jolanta':[5,45,3]
#
# }
# for name,favnumbers in fav_numbers.items():
#     print(f"Ulubione numery użytkownika: {name.title()}")
#     for number in favnumbers:
#         print(f"\n{number}")

#6.11

cities= {
    'Rawicz':{
        'country':'Poland',
        'population':30000,
        'fact':'Stąd pochodzę'
    },
    'Chicago': {
        'country': 'USA',
        'population': 3000000,
        'fact': 'Stąd pochodzi Chicago Bulls'
    },
    'Kingston': {
        'country': 'Jamaica',
        'population': 1200000,
        'fact': 'Stąd pochodzi Bob Spizgus Marley'
    },
}

for city,city_info in cities.items():
    print(f"Nazwa miasta: {city}\nPaństwo:{city_info['country']}\nPopulacja:{city_info['population']}\nFun fact o tym mieście:{city_info['fact']}\n")