#KLASA CAR

class Car():
    """prosta próba zaprezentowania samochodu"""

    def __init__(self,make, model, year):
        """Inicjalizacja atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        "Zwrot elegancko sformatowanego opisu samochodu"
        long_name = str(self.year) + '  ' + self.make + ' ' + self.model
        return long_name
car= Car("Reanault","Scenic",2000)
print(car.get_descriptive_name())
