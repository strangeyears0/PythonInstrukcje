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
        print(f"Marka: {self.make.title()}"
              f"\nModel: {self.model.title()}"
              f"\nRok Produkcji: {self.year}")

car= Car("Reanault","Scenic",2000)
car.get_descriptive_name()
