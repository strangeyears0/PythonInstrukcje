"""zestaw klas do zaprezentowania samochodu elektrycznego"""

from car import Car
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