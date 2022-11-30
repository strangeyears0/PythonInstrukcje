"""Klasa, która będzie używana do zaprezentowania samochodu"""

class Car():
    """Prosta próba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = str(self.year) + '  ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informacje o przebiegu samochodu"""
        print("Ten samochód ma przejechane"+ str(self.odometer_reading)+" km.")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu
        zmiana zostanie odrzucona w przypadku próby cofnięcia licznika"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika!")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartosci licznika przebiegu o podana wartość"""
        self.odometer_reading += kilometers

class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego."""

    def __init__(self,battery_size=70):
        """Inicjalizacja atrybutów akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlanie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o wielkości {self.battery_size} kwh.")

    def get_range(self):
        """Wyświetla informacje o zasięgu"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f"Zasięg tego samochodu wynosi około {range} km"
        print(message)
class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
    def __init__(self,make,model,year):
        """Inicjalizacja klasy nadrzędnej"""
        super().__init__(make,model,year)
        self.battery = Battery()