#ARGUMENTY POZYCYJNE

# def describe_pet(animal_type, pet_name):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type}")
#     print(f"Mój {animal_type} ma na imię {pet_name}")
#
# describe_pet('kot','Hera')

#WIELE WYWOŁAŃ FUNKCJI

# def describe_pet(animal_type, pet_name):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type.title()}")
#     print(f"Mój {animal_type.title()} ma na imię {pet_name.title()}")
#
# describe_pet('kot','Hera')
# describe_pet('królik','ginger')

#W PRZYPADKU ARGUMENTÓW POZYCYJNYCH KOLEJNOŚĆ MA ZNACZENIE

# def describe_pet(animal_type, pet_name):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type.title()}")
#     print(f"Mój {animal_type.title()} ma na imię {pet_name.title()}")
#
# describe_pet('hera','kot')

#ARGUMENTY W POSTACI SŁÓW KLUCZOWYCH
#
# def describe_pet(animal_type, pet_name):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type.title()}")
#     print(f"Mój {animal_type.title()} ma na imię {pet_name.title()}")
#
# describe_pet(animal_type='kot',pet_name='Hera')
# describe_pet(pet_name='Hera',animal_type='kot')


#WARTOŚCI DOMYŚLNE

# def describe_pet(pet_name,animal_type='kot'):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type.title()}")
#     print(f"Mój {animal_type.title()} ma na imię {pet_name.title()}")
#
# describe_pet(pet_name='Hera')
# describe_pet('Hera')
# describe_pet('Ginger',animal_type='królik')
# describe_pet('pjes')

#ODPOWIEDNIKI WYWOŁAŃ FUNKCJI

# def describe_pet(pet_name,animal_type='kot'):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type.title()}")
#     print(f"Mój {animal_type.title()} ma na imię {pet_name.title()}")
# describe_pet('hera')
# describe_pet(pet_name='hera')
# describe_pet('ginger','królik')
# describe_pet(pet_name='ginger',animal_type='królik')
# describe_pet(animal_type='królik',pet_name='ginger',)

#UNIKANIE BŁĘDÓW

# def describe_pet(pet_name,animal_type):
#     """Wyświetla informacje o zwierzęciu"""
#     print(f"\nMoje zwierzę to {animal_type.title()}")
#     print(f"Mój {animal_type.title()} ma na imię {pet_name.title()}")
# describe_pet() #WYWOŁANIE PUSTEJ FUNKCJI BEZ ARGUMENTÓW

#8.3

# def make_shirt(size,text):
#     """Wyświetla informacje o koszulce(rozmiar i napis)"""
#     print(f"Koszulka ma rozmiar {size} i nadruk o treści {text}")
# make_shirt('Large','HWDP')
# make_shirt(size='Extra Large',text='JP100%')

#8.4
#
# def make_shirt(size,text='Uwielbiam Pythona'):
#     """Wyświetla informacje o koszulce(rozmiar i napis)"""
#     print(f"Koszulka ma rozmiar {size} i nadruk o treści {text}")
# make_shirt('XL')
# make_shirt('L')
# make_shirt('S',text='Sram na was')

#8.5
# def describe_city(city,country='Polska'):
#     print(f"{city} znajduje się w kraju: {country}")
# describe_city('Rawicz')
# describe_city('Warszawa')
# describe_city('Londyn',country='Anglia')


