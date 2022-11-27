#METODA __init__() W KLASIE POTOMNEJ

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
# class ElectricCar(Car):
#     """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
#
#     def __init__(self, make, model, year):
#         """Inicjalizacja atrybutów klasy nadrzędnej"""
#         super().__init__(make,model,year)
#
# my_tesla = ElectricCar('tesla','model s',2016)
# print(my_tesla.get_descriptive_name())

#DEFINIOWANIE ATRYBUTÓW I METOD DLA KLASY POTOMNEJ


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
# class ElectricCar(Car):
#     """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
#
#     def __init__(self, make, model, year):
#         """Inicjalizacja atrybutów klasy nadrzędnej.
#         Następnie inicjalizacja atrybutów charakterystycznych dla samochodu
#         elektrycznego"""
#         super().__init__(make,model,year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """Wyświetla informacje oo wielkości akumulatora."""
#         print(f"Ten samochód ma akumlator o pojemności {str(self.battery_size)} Kwh")
#
# my_tesla = ElectricCar('Tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
#
# my_tesla.describe_battery()

#NADPISYWANIE METOD KLASY NADRZĘDNEJ

class Car():
    """prosta próba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        "Zwrot elegancko sformatowanego opisu samochodu"
        long_name = str(self.year) + '  ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """wyświetla informacje o przebiegu samochodu"""
        print(f"Ten samochód ma przejechane {str(self.odometer_reading)} km")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie mozna cofnąc licznika przebiegu ! ")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartosci licznika przebiegu o podana wartość"""
        self.odometer_reading += kilometers

class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów klasy nadrzędnej.
        Następnie inicjalizacja atrybutów charakterystycznych dla samochodu
        elektrycznego"""
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """Wyświetla informacje oo wielkości akumulatora."""
        print(f"Ten samochód ma akumlator o pojemności {str(self.battery_size)} Kwh")

    def fill_gas_tank(self):
            """samochód o napędzie elektrynczmy nie ma zbiornika paliwa"""
            print("Ten samochód nie wymaga tankowania paliwa")

my_tesla = ElectricCar('Tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()