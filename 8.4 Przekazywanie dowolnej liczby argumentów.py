# def make_pizza(*toppings):
#     """Wyświetlenie listy dodatków wybranych przez klienta"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('pieczarki','ser','ananas')

# def make_pizza(*toppings):
#     """Podsumowanie informacji o przygotowanej pizzy"""
#     print("\nPrzygotowuję pizzę z następującymi dodatkami")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza('pepperoni')
# make_pizza('pieczarki','ser','ananas')
#

#ARGUMENTY POZYCYJNE I PRZEKAZYWANIE DOWOLNEJ LICZBY ARGUMENTÓW
#
# def make_pizza(size, *toppings):
#     """Podsumowanie informacji o przygotowanej pizzy"""
#     print(f"\nPrzygotowuję pizzę o wielkości {str(size)} cm z następującymi dodatkami:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(40,'pepperoni')
# make_pizza(30,'pieczarki','ser')

#UŻYWANIE DOWOLNEJ LICZBY ARGUMENTÓW W POSTACI SŁÓW KLUCZOWYCH
#
# def build_profile(first, last, **user_info):
#     """Budowa SŁOWNIKA zawierającego wszelkie informacje o użytkowniku"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert','einstein',location='princeton',field='fizyka')
# print(user_profile)

#8.12
# def sandwich(*toppings):
#     """Podsumowanie informacji o kanapce"""
#     print(f"\nPrzygotowuję kanapkę z :")
#     for topping in toppings:
#         print(f"- {topping}")
# sandwich('ser')
# sandwich('szynko','pomidor')
# sandwich('tuńczyk','ogórek','majonez')

#8.13

# def build_profile(first, last, **user_info):
#     """Budowa SŁOWNIKA zawierającego wszelkie informacje o użytkowniku"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('Bartłomiej','Sławiński',lat='29',ulubionyjęzyk='python',zawód='malarz')
# print(user_profile)

#8.14

# def build_car(company, model, **car_info):
#     """Budowa słownika zawierającego informacje o samochodzie"""
#     car={}
#     car['company'] = company
#     car['model'] = model
#     for key, value in car_info.items():
#         car[key] = value
#     return car
# user_car = build_car('Renault','Scenic',color='Zielony',age='20')
# print(user_car)