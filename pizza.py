def make_pizza(size, *toppings):
    """Podsumowanie informacji o przygotowanej pizzy"""
    print(f"\nPrzygotowuję pizzę o wielkości {str(size)} cm z następującymi dodatkami:")
    for topping in toppings:
        print(f"- {topping}")