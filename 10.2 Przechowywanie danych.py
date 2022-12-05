#UŻYWANIE json.dump() i json.load()
# """stworzenie json"""
# import json
#
# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'numbers.json'
#
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)
#
# """odczyt json"""
#
# filename = 'numbers.json'
#
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)

#ZAPISYWANIE I ODCZYTYWANIE DANYCH WYGENEROWANYCH PRZEZ UŻYTKOWNIKA

"""przywitanie i zapamiętanie użytkownika"""
#
# import json
#
# username = input("Jak masz na imię?")
#
# filename = 'username.json'
#
# with open(filename, 'w') as f_obj:
#     json.dump(username,f_obj)
#     print(f"Twoje imie zostało zapisane i będzie używane później {username.title()} !")
#
# """Odcdzyt DANYCH"""
#
# import json
#
# filename = 'username.json'
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print(f"Witamy ponownie {username.title()} ")
#
"""Połączenie dwóch powyższych"""
#
# import json
# filename='username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("Jak masz na imię?")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#     print(f"Twoje imię zostało zapisane i będzie używane później "
#           f"{username.title()} ")
# else:
#     print(f"Witamy ponownie {username.title()} !")

#REFAKTORYZACJA

# import json
#
# def greet_user():
#     """Przywitanie użytkownika z użyciem jego imienia"""
#     filename='username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("Jak masz na imię?")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#         print(f"Twoje imię zostało zapisane i będzie używane później "
#               f"{username.title()} ")
#     else:
#         print(f"Witamy ponownie {username.title()} !")
# greet_user()



"""REFAKTORYZACJA powyższego aby nie wykonywała zbyt wielu zadań na raz"""
#
# import json
#
# def get_stored_username():
#     """Pobranie imienia z pliku o ile taki istnieje."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def greet_user():
#     """Przywitanie użytkownika z użyciem jego imienia"""
#     username = get_stored_username()
#     if username:
#         print(f"Witamy ponownie {username} !")
#     else:
#         username = input("Jak masz na imię?")
#         filename = 'username.json'
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print(f"Twoje imie zostało zapisane {username} !")
# greet_user()
#

"""REFAKTORYZACJA powyższego"""

#
# import json
#
# def get_stored_username():
#     """Pobranie imienia z pliku o ile taki istnieje."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
#
# def get_new_username():
#     """Poproszenie użytkownika aby podał swoje imie
#     a nastepnie zapisanie tego imiienia w pliku"""
#
#     username = input("Jak masz na imię?")
#     filename = 'username.json'
#     with open(filename,'w') as f_obj:
#         json.dump(username, f_obj)
#     return username
#
# def greet_user():
#     """Przywitanie użytkownia z użyciem jego imiienia"""
#     username = get_stored_username()
#     if username:
#         print(f"Witamy {username}")
#     else:
#         username = get_new_username()
#         print(f"Twoje imie zostało zapisane i będzie używane poniżej")
#         print(f"{username}")
# greet_user()
# get_new_username()
# greet_user()

#10.11

# import json
#
# def get_number():
#     """Pobranie ulubionej liczby od uzytkownika i zapisanie jej do pliku"""
#     fav_number = input("Podaj ulubioną liczbę")
#     filename = 'fav_number.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(fav_number, f_obj)
#     return fav_number
# def read_number():
#     """Odczytanie ulubionej liczby."""
#     fav_number = get_number()
#     print(f"Twoja ulubiona liczba to {fav_number}")
#
#
# read_number()

#10.12
#
# def get_number():
#     """Pobranie ulubionej liczby od uzytkownika i zapisanie jej do pliku"""
#     fav_number = input("Podaj ulubioną liczbę")
#     filename = 'fav_number.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(fav_number, f_obj)
#     return fav_number