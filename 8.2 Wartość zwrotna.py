#ZWROT PROSTEJ WARTOŚCI
#
# def get_formated_name(first_name, last_name):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko"""
#     full_name = first_name + ' '+ last_name
#     return full_name.title()
# musician= get_formated_name('jimi','hendrix')
# print(musician)

#DEFINIOWANIE ARGUMENTU JAKO OPCJONALNEGO

# def get_formated_name(first_name, last_name, middle_name=''):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko"""
#     if middle_name:
#         full_name = first_name + ' '+ middle_name+ ' '+ last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician= get_formated_name('jimi','hendrix')
# print(musician)
# musician= get_formated_name('john','hooker','lee')
# print(musician)

#ZWROT SŁOWNIKA

# def build_person(first_name,last_name):
#     """Zwraca słownik informacji o danej osobie."""
#     person = {'first':first_name, 'last':last_name}
#     return person
# musician=build_person('jimi','hendrix')
# print(musician)

# def build_person(first_name,last_name,age=''):
#     """Zwraca słownik informacji o danej osobie."""
#     person = {'first':first_name, 'last':last_name}
#     if age:
#         person['age']=age
#     return person
# musician=build_person('jimi','hendrix',age=27)
# print(musician)


#UŻYWANIE FUNKCJI WRAZ Z PĘTLĄ WHILE


# def get_formatted_name(first_name, last_name):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko"""
#     full_name = first_name + ' '+ last_name
#     return full_name.title()
# while True:
#     print("\nProszę podać imię i nazwisko")
#     print("(Wpisz 'q' aby zakończyć pracę.)")
#
#     f_name=input("Imię: ")
#     if f_name == 'q':
#         break
#     l_name=input("Nazwisko: ")
#     if l_name == 'q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print(f"\nWitaj {formatted_name}")

#8.6
# def city_country(city,country):
#     """Zwraca miasto i kraj"""
#     build = city + ',' + country
#     print (build.title())
# city_country('Santiago','Chile')
# city_country('Rawicz','Polska')
# city_country(city='Londyn',country='Anglia')

#8.7
# def make_album(name,title,track_numbers=''):
#     """Zwraca słownik z informacją o albumie"""
#     album={'name':name,'title':title}
#     if track_numbers:
#         album['track_numbers']=track_numbers
#     return album
# created_album=make_album('O.S.T.R','masz to jak w banku','18')
# print(created_album)
# created_album=make_album('Slu','na legalu')
# print(created_album)

#8.8
#
# def make_album(name,title,track_numbers=''):
#     """Zwraca słownik z informacją o albumie"""
#     album={'name':name,'title':title}
#     if track_numbers:
#         album['track_numbers']=track_numbers
#     return album
# while True:
#     print("Podaj nazwę artysty,albumu i liczbę utworów:")
#     print("\nWpisz 'q' aby wyjść")
#
#     name = input("Podaj nazwę artysty")
#     if name == 'q':
#         break
#     title = input("Podaj nazwę albumu")
#     if title == 'q':
#         break
#     track_numbers = input("Podaj liczbę utwórów")
#     if track_numbers == 'q':
#         break
#     created_album=make_album(name,title,track_numbers)
#     print(created_album)