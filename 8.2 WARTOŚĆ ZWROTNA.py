#ZWROT PROSTEJ WARTOŚCI
#
# def get_formated_name(first_name, last_name):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko"""
#     full_name = first_name + ' '+ last_name
#     return full_name.title()
# musician= get_formated_name('jimi','hendrix')
# print(musician)

#DEFINIOWANIE ARGUMENTU JAKO OPCJONALNEGO

# def get_formated_name(first_name, last_name, middle_name=''):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko"""
#     if middle_name:
#         full_name = first_name + ' '+ middle_name+ ' '+ last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician= get_formated_name('jimi','hendrix')
# print(musician)
# musician= get_formated_name('john','hooker','lee')
# print(musician)

#ZWROT SŁOWNIKA

# def build_person(first_name,last_name):
#     """Zwraca słownik informacji o danej osobie."""
#     person = {'first':first_name, 'last':last_name}
#     return person
# musician=build_person('jimi','hendrix')
# print(musician)

# def build_person(first_name,last_name,age=''):
#     """Zwraca słownik informacji o danej osobie."""
#     person = {'first':first_name, 'last':last_name}
#     if age:
#         person['age']=age
#     return person
# musician=build_person('jimi','hendrix',age=27)
# print(musician)


#UŻYWANIE FUNKCJI WRAZ Z PĘTLĄ WHILE


# def get_formatted_name(first_name, last_name):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko"""
#     full_name = first_name + ' '+ last_name
#     return full_name.title()
# while True:
#     print("\nProszę podać imię i nazwisko")
#     print("(Wpisz 'q' aby zakończyć pracę.)")
#
#     f_name=input("Imię: ")
#     if f_name == 'q':
#         break
#     l_name=input("Nazwisko: ")
#     if l_name == 'q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print(f"\nWitaj {formatted_name}")