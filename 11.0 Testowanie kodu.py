#TESTOWANIE FUNKCJI

# def get_formated_name(first, last):
#     """Generuje sformatowane pełne imię i naziwsko"""
#     full_name = first + ' ' + last
#     return full_name.title()

from name_function import get_formated_name

print("Wpisz 'q' aby zakończyć działanie programu.")

while True:
    first = input("Podaj imię: ")
    if first == 'q':
        break
    last = input("Podaj nazwisko: ")
    if last == 'q':
        break

    formatted_name = get_formated_name(first,last)
    print("\tElegancko sformatowane imię i nazwisko: \n\t\t" + formatted_name)
