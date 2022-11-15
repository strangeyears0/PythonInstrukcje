#PRZENOSZENIE ELEMENTÓW Z JEDNEJ LISTY NA DRUGĄ


# unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Weryfikacja użytkownika {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nZweryfikowano wymienionych poniżej uzytkowników: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#USUWANIE Z LISTY WSZYSTKICH EGZEMPLARZY OKREŚLONEJ WARTOŚCI

# pets = ['pies', 'kot', 'pies', 'złota rybka', 'kot', 'królik', 'kot',]
# print(pets)
#
# while 'kot' in pets:
#     pets.remove('kot')
#
# print(pets)

#UMIESZCZENIE W SŁOWNIKU DANYCH WEJŚCIOWYCH WPROWADZONYCH PRZEZ UŻYTKOWNIKA

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\nJak masz na imię?")
#     response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia?")
#
#     responses[name]=response
#
#     repeat = input("Czy ktoś jeszcze chce wziać udział w ankiecie? (TAK/NIE)")
#     if repeat == 'NIE':
#         polling_active = False
# print("\n\tWyniki ankiety")
# for name, response in responses.items():
#     print(f"{name} chciałby wspiąć się na {response}.")

#7.8

# sandwich_orders = ['serowa','tuńczyk','salami','wege',]
# finished_orders=[]
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#
#     print(f"Przygotowano kanapkę {current_sandwich}")
#     finished_orders.append(current_sandwich)
#
# print(finished_orders)

#7.9

# sandwich_orders = ['pastrami','serowa','tuńczyk','pastrami','salami','wege','pastrami']
# finished_orders=[]
# print(f"{sandwich_orders}")
# print("Skończyło się pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#
#     print(f"Przygotowano kanapkę {current_sandwich}")
#     finished_orders.append(current_sandwich)
#
# print(finished_orders)

#7.10
#
# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("Podaj swoje imię")
#     response = input("Gdzie chciałyś pojechać?")
#
#     responses[name] = response
#
#     repeat = input("Czy ktoś jeszcze chce wziąć udział w ankiecie?(Tak/Nie)")
#     if repeat == 'Nie':
#         polling_active = False
# print("\n\tWyniki ankiety")
# print(f"{name} chciałby pojechać do {response}")