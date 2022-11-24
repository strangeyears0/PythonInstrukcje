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
