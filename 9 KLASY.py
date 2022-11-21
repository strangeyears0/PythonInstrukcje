#UTWORZENIE I UŻYCIE KLASY

#Utworzenie klasy DOG

class Dog():
    """Prosta próba modelowania Psa"""

    def __init__(self, name, age):
        """Inicjalizacja atrybutów name i age."""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecnia."""
        print(f"{self.name.title()} +  teraz siedzi")

    def roll_over(self):
        """Symulacja że pies kładzie się na plecy po optrzymaniu polecenia"""
        print(f"{self.name.title()} teraz położył się na plecy.")
