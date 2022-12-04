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