#KLASA CAR

# class Car():
#     """prosta próba zaprezentowania samochodu"""
#
#     def __init__(self,make, model, year):
#         """Inicjalizacja atrybutów opisujących samochód"""
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         "Zwrot elegancko sformatowanego opisu samochodu"
#         long_name = str(self.year) + '  ' + self.make + ' ' + self.model
#         return long_name
# car= Car("Reanault","Scenic",2000)
# print(car.get_descriptive_name())

#PRZYPISANIE ATRYBUTOWI WARTOŚCI DOMYŚLNEJ

# class Car():
#     """prosta próba zaprezentowania samochodu"""
#
#     def __init__(self,make, model, year):
#         """Inicjalizacja atrybutów opisujących samochód"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         "Zwrot elegancko sformatowanego opisu samochodu"
#         long_name = str(self.year) + '  ' + self.make + ' ' + self.model
#         return long_name
#
#     def read_odometer(self):
#         """wyświetla informacje o przebiegu samochodu"""
#         print(f"Ten samochód ma przejechane {str(self.odometer_reading)} km")
#
# car= Car("Reanault","Scenic",2000)
# print(car.get_descriptive_name())
# print(car.read_odometer())


#MODYFIKACJA WARTOSCI ATRYBUTU :

#BEZPOŚREDNIA MODYFIKACJA WARTOŚCI ATRYBUTU

# class Car():
#     """prosta próba zaprezentowania samochodu"""
#
#     def __init__(self, make, model, year):
#         """Inicjalizacja atrybutów opisujących samochód"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         "Zwrot elegancko sformatowanego opisu samochodu"
#         long_name = str(self.year) + '  ' + self.make + ' ' + self.model
#         return long_name
#
#     def read_odometer(self):
#         """wyświetla informacje o przebiegu samochodu"""
#         print(f"Ten samochód ma przejechane {str(self.odometer_reading)} km")
#
#
# car = Car("Reanault", "Scenic", 2000)
# print(car.get_descriptive_name())
# print(car.read_odometer())
#
# car.odometer_reading = 23
# print(car.read_odometer())
#

#MODYFIKACJA WARTOŚCI ATRYBUTU ZA POMOCĄ METODY
# class Car():
#     """prosta próba zaprezentowania samochodu"""
#
#     def __init__(self, make, model, year):
#         """Inicjalizacja atrybutów opisujących samochód"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 25
#
#     def get_descriptive_name(self):
#         "Zwrot elegancko sformatowanego opisu samochodu"
#         long_name = str(self.year) + '  ' + self.make + ' ' + self.model
#         return long_name
#
#     def read_odometer(self):
#         """wyświetla informacje o przebiegu samochodu"""
#         print(f"Ten samochód ma przejechane {str(self.odometer_reading)} km")
#
#     def update_odometer(self, mileage):
#         """Przypisanie podanej wartości licznikowi przebiegu"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Nie mozna cofnąc licznika przebiegu ! ")
#
# car = Car("Reanault", "Scenic", 2000)
# print(car.get_descriptive_name())
#
#
# car.update_odometer(23)
# car.read_odometer()


#INKREMENTACJA WARTOŚCI ATRYBUTU ZA POMOCĄ METODY


# class Car():
#     """prosta próba zaprezentowania samochodu"""
#
#     def __init__(self, make, model, year):
#         """Inicjalizacja atrybutów opisujących samochód"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         "Zwrot elegancko sformatowanego opisu samochodu"
#         long_name = str(self.year) + '  ' + self.make + ' ' + self.model
#         return long_name
#
#     def read_odometer(self):
#         """wyświetla informacje o przebiegu samochodu"""
#         print(f"Ten samochód ma przejechane {str(self.odometer_reading)} km")
#
#     def update_odometer(self, mileage):
#         """Przypisanie podanej wartości licznikowi przebiegu"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Nie mozna cofnąc licznika przebiegu ! ")
#
#     def increment_odometer(self, kilometers):
#         """Inkrementacja wartosci licznika przebiegu o podana wartość"""
#         self.odometer_reading += kilometers
#
# car = Car("Reanault", "Scenic", 2000)
# print(car.get_descriptive_name())
# car.update_odometer(270000)
# car.read_odometer()
#
# car.increment_odometer(1000)
# car.read_odometer()
#
# car.update_odometer(23)
# car.read_odometer()


#9.4

#
# class Restaurant():
#     """Prosta próba stworzenia restauracji"""
#
#     def __init__(self, restaurant_name, cusine_type,):
#         """Inicjalizacja nazwy oraz typu kuchni"""
#         self.name = restaurant_name
#         self.type = cusine_type
#         self.number_served = 10
#
#     def describe_restaurant(self):
#         """Metoda wyświetlająca informacje o nazwie i typie kuchni"""
#         print(f"Restauracja {self.name.title()}, podaję kucnię typu {self.type.title()}")
#
#     def open_restaurant(self):
#         """Metoda podająca informacje o godzinach otwarcia restauracji"""
#         print(f"Restauracja czynna w godzinach 8-16")
#
#     def read_number_served(self):
#         """Wyświetla informacje o liczbie klientów"""
#         print(f"Liczba klientów: {str(self.number_served)}")
#
#         #To jest bez sensu xD
#     # def set_number_served(self):
#     #     """#Zdefiniowanie liczby obsłużonych klientów """
#     #     self.number_served=input("Podaj liczbę obsłużonych klientów")
#
#     def set_number_served(self, number_served):
#         """Zdefiniowanie liczby obsłużonych klientów """
#         self.number_served = number_served
#
#     def increment_number_served(self, inc_number_served):
#         """Inkrementacja liczby obsłużonych klientów """
#         self.number_served += inc_number_served
# restaurant = Restaurant("Orzełek","piwko",)
# print(restaurant.name)
# print(restaurant.type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.read_number_served()
# restaurant.set_number_served(25)
# restaurant.read_number_served()
# restaurant.increment_number_served(50)
# restaurant.read_number_served()

#9.5

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
#         self.login_attempts = 0
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
#     def increment_login_attempts(self,):
#         """metoda pozwalajaca na inkrementację wartosci login_attempts"""
#         self.login_attempts += 1
#         print(f"Liczba logowań:  {self.login_attempts}")
#
#     def reset_login_attempts(self):
#         """Metoda pozwalająca na resetowanie wartości login attempts"""
#         self.login_attempts = 0
#         print(f"Liczba logowań: {self.login_attempts}")
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
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.reset_login_attempts()
# user.increment_login_attempts()