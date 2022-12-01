class Restaurant():
    """Prosta próba stworzenia restauracji"""

    def __init__(self, restaurant_name, cusine_type):
        """Inicjalizacja nazwy oraz typu kuchni"""
        self.name = restaurant_name
        self.type = cusine_type
        self.number_served = 10

    def describe_restaurant(self):
        """Metoda wyświetlająca informacje o nazwie i typie kuchni"""
        print(f"Restauracja {self.name.title()}, podaję kucnię typu {self.type.title()}")

    def open_restaurant(self):
        """Metoda podająca informacje o godzinach otwarcia restauracji"""
        print(f"Restauracja czynna w godzinach 8-16")

    def read_number_served(self):
        """Wyświetla informacje o liczbie klientów"""
        print(f"Liczba klientów: {str(self.number_served)}")

        #To jest bez sensu xD
    # def set_number_served(self):
    #     """#Zdefiniowanie liczby obsłużonych klientów """
    #     self.number_served=input("Podaj liczbę obsłużonych klientów")

    def set_number_served(self, number_served):
        """Zdefiniowanie liczby obsłużonych klientów """
        self.number_served = number_served

    def increment_number_served(self, inc_number_served):
        """Inkrementacja liczby obsłużonych klientów """
        self.number_served += inc_number_served
# restaurant = Restaurant("Orzełek","piwko",)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.read_number_served()
# restaurant.set_number_served(25)
# restaurant.read_number_served()
# restaurant.increment_number_served(50)
# restaurant.read_number_served()

class IceCreamStand(Restaurant):
    """Prosta próba dodania restauracj lodziarni"""

    def __init__(self, restaurant_name, cusine_type,):
        super().__init__(restaurant_name,cusine_type)

        self.flavours = {'czekoladowy','truskawkowy','malinowy'}

    def show_flavours(self):
        """Metoda wyświetlająca smaki"""
        print(f"Możliwe smaki w lodziarni  {self.flavours}")
# ice = IceCreamStand('LODówka','Lodziarnia')
# ice.show_flavours()
