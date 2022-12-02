#ODCZYTYWANIE DANYCH Z PLIKU

#WCZYTYWANIE CAŁEGO PLIKU
#
# with open('pi_digits') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

#ŚCIEŻKA DOSTĘPU DO PLIKU
from importlib.resources import contents

# file_path = r'C:\Users\Ja\Documents\panplik.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

#ODCZYTYWANIE WIERSZ PO WIERSZU
#
# filename = 'pi_digits'
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#UTWORZENIE LISTY WIERSZY NA PODSTAWIE ZAWARTOŚCI PLIKU

# filename = 'pi_digits'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

#PRACA Z ZAWARTOŚCIĄ PLIKU

# filename = 'pi_digits'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
#
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
# print(len(pi_string))
#


#OGROMNE PLIKI CZYLI NA PRZKŁAD MILION CYFR

# filename = 'pi_milion'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string[:42] + "...")
# print(len(pi_string))

#CZY DATA TWOICH URODZIN ZNAJDUJE SIĘ W LICZBIE PI?

# filename = 'pi_milion'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# birthday = input("Podaj datę urodzenia (w formacie ddmmrr): ")
# if birthday in pi_string:
#     print("Twoja data urodzenia znajdue się w pierwszym milionie liczby pi!")
# else:
#     print("Twoja data urodzenia nie znajduje się w pierwszym milionie liczb pi")

#10.1


# with open('what') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# what = 'what'
#
# with open(what) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename = 'what'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

#10.2

filename = 'what'

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('tworzyc','robic').rstrip())
