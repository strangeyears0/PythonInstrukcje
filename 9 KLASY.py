#UTWORZENIE I UŻYCIE KLASY

#Utworzenie klasy DOG

# class Dog():
#     """Prosta próba modelowania Psa"""
#
#     def __init__(self, name, age):
#         """Inicjalizacja atrybutów name i age."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Symulacja, że pies siada po otrzymaniu polecnia."""
#         print(f"{self.name.title()} +  teraz siedzi")
#
#     def roll_over(self):
#         """Symulacja że pies kładzie się na plecy po optrzymaniu polecenia"""
#         print(f"{self.name.title()} teraz położył się na plecy.")
#UTWORZENIE EGZEMPLARZA NA PODSTAWIE KLASY

# class Dog():
#     """Prosta próba modelowania Psa"""
#
#     def __init__(self, name, age):
#         """Inicjalizacja atrybutów name i age."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Symulacja, że pies siada po otrzymaniu polecnia."""
#         print(f"{self.name.title()} teraz siedzi")
#
#     def roll_over(self):
#         """Symulacja że pies kładzie się na plecy po optrzymaniu polecenia"""
#         print(f"{self.name.title()} teraz położył się na plecy.")
#
#     def shit(self):
#         """Symulacja srania na dywan"""
#         print(f"{self.name.title()} zesrał się na dywan.")
# my_dog = Dog('willie',6)
#
# print(f"Mój pies ma na imię {my_dog.name.title()}")
# print(f"Mój pies ma {str(my_dog.age)} lat")


#UZYSKANIE DOSTĘPU DO  ATRYBUTÓW
#
# print(my_dog.name)


#WYWOŁYWANIE METOD

# my_dog.sit()
# my_dog.roll_over()
# my_dog.shit()


#UTWORZENIE WIELU EGZEMPLARZY

# class Dog():
#     """Prosta próba modelowania Psa"""
#
#     def __init__(self, name, age):
#         """Inicjalizacja atrybutów name i age."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Symulacja, że pies siada po otrzymaniu polecnia."""
#         print(f"{self.name.title()} teraz siedzi")
#
#     def roll_over(self):
#         """Symulacja że pies kładzie się na plecy po optrzymaniu polecenia"""
#         print(f"\n{self.name.title()} teraz położył się na plecy.")
#
#     def shit(self):
#         """Symulacja srania na dywan"""
#         print(f"\n\t{self.name.title()} zesrał się na dywan.")
#
# my_dog = Dog('azor',6)
# your_dog = Dog('szmata',4)
#
# print(f"Mój pies ma na imię {my_dog.name.title()} a twój ma na imię {your_dog.name.title()}")
# print(f"\nMój pies ma {my_dog.age} lat a twój ma {your_dog.age} lat")
#
# my_dog.roll_over()
# your_dog.shit()

#9.1

# class Restaurant():
#     """Prosta próba stworzenia restauracji"""
#
#     def __init__(self, restaurant_name, cusine_type):
#         """Inicjalizacja nazwy oraz typu kuchni"""
#         self.name = restaurant_name
#         self.type = cusine_type
#
#     def describe_restaurant(self):
#         """Metoda wyświetlająca informacje o nazwie i typie kuchni"""
#         print(f"Restauracja {self.name.title()}, podaję kucnię typu {self.type.title()}")
#
#     def open_restaurant(self):
#         """Metoda podająca informacje o godzinach otwarcia restauracji"""
#         print(f"Restauracja czynna w godzinach 8-16")
#
# restaurant = Restaurant("Orzełek","piwko")
# print(restaurant.name)
# print(restaurant.type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

#9.2

# class Restaurant():
#     """Prosta próba stworzenia restauracji"""
#
#     def __init__(self, restaurant_name, cusine_type):
#         """Inicjalizacja nazwy oraz typu kuchni"""
#         self.name = restaurant_name
#         self.type = cusine_type
#
#     def describe_restaurant(self):
#         """Metoda wyświetlająca informacje o nazwie i typie kuchni"""
#         print(f"Restauracja {self.name.title()}, podaję kucnię typu {self.type.title()}")
#
#     def open_restaurant(self):
#         """Metoda podająca informacje o godzinach otwarcia restauracji"""
#         print(f"Restauracja czynna w godzinach 8-16")
#
# restaurant = Restaurant("Orzełek","piwko")
# restaurant1 = Restaurant("speluno","wódka")
# restaurant2 = Restaurant("Verona","pizza")
#
#
#
# restaurant.describe_restaurant()
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()

#9.3

#
#
# class User():
#     """Stworzenie klasy użytkownika"""
#
#     def __init__(self, first_name, last_name, age, nickname, favourite_pet):
#         """Inicjalizacja atrybutów użytkownika"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.nickname = nickname
#         self.favourite_pet = favourite_pet
#
#     def describe_user(self):
#         """Metoda podsumowująca informacje o użytkowniku"""
#         print(f"Dane użytkownika:"
#               f"\nImię : {self.first_name.title()}"
#               f"\nNazwisko : {self.last_name.title()}"
#               f"\nWiek : {str(self.age)}"
#               f"\nNick : {self.nickname.title()}"
#               f"\nUlubione zwierzątko : {self.favourite_pet.title()}")
#
#     def greet_user(self):
#         """Metoda witająca użytkownika"""
#         print(f"Witam {self.nickname.title()} twóje ulubine zwierzątko to: {self.favourite_pet.title()}")
#
# user = User('Bartek','Sławiński',29,'szaman','kotek')
# user2 = User('anna','beznazwiska',18,'czarownica','zebra')
# user3 = User('hera','kotka',1,'rojber','człowieki')
# user.describe_user()
# user.greet_user()
# user2.describe_user()
# user2.greet_user()
# user3.describe_user()
# user3.greet_user()
