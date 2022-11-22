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

class Dog():
    """Prosta próba modelowania Psa"""

    def __init__(self, name, age):
        """Inicjalizacja atrybutów name i age."""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecnia."""
        print(f"{self.name.title()} teraz siedzi")

    def roll_over(self):
        """Symulacja że pies kładzie się na plecy po optrzymaniu polecenia"""
        print(f"\n{self.name.title()} teraz położył się na plecy.")

    def shit(self):
        """Symulacja srania na dywan"""
        print(f"\n\t{self.name.title()} zesrał się na dywan.")

my_dog = Dog('azor',6)
your_dog = Dog('szmata',4)

print(f"Mój pies ma na imię {my_dog.name.title()} a twój ma na imię {your_dog.name.title()}")
print(f"\nMój pies ma {my_dog.age} lat a twój ma {your_dog.age} lat")

my_dog.roll_over()
your_dog.shit()