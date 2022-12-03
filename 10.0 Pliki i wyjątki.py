#ODCZYTYWANIE DANYCH Z PLIKU

#WCZYTYWANIE CAŁEGO PLIKU
#
# with open('pi_digits') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

#ŚCIEŻKA DOSTĘPU DO PLIKU
from fileinput import filename
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

# filename = 'what'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.replace('tworzyc','robic').rstrip())

# ZAPISYWANIE DANYCH W PLIKU

#ZAPISYWANIE DANYCH DO PUSTEGO PLIKU

# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("Uwielbiam programować.")


#ZAPISYWANIE WIELU WIERSZY

# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("Uwielbiam programować.")
#     file_object.write("\nUwielbiam tworzyć nowe gry")

#DOŁĄCZANIE DO PLIKU

# filename = 'programming.txt'
#
# with open(filename, 'a') as file_object:
#     file_object.write("Uwielbiam odnajdywać elementy w ogromnych zbiorach danych.\n")
#     file_object.write("Uwielbiam tworzyć aplikacje uruchamiane w przeglądarce.")

#10.3

# name = input('Podaj swoje imie:')
# filename = 'guest.txt'
#
# with open(filename, 'w')as file_object:
#     file_object.write(str(name))

#10.4
# filename = 'guest_book.txt'
# flag = True
# while flag:
#     name=input('Podaj swoje imie:')
#     with open(filename, 'a') as file_object:
#         file_object.write(f"\n{str(name)}")
#     print("Jeśli chcesz zakończyć wpisz 'q' ")
#     if name == 'q':
#         flag = False

#10.5

# filename = 'answers.txt'
#
# flag = True
#
# while flag:
#     answer = input("Dlaczego lubisz programowanie?:")
#     with open(filename, 'a') as file_object:
#         file_object.write(f"\n{str(answer)}")
#     print("Jeśli chcesz zakończyć wpisz 'q' ")
#     if answer == 'q':
#         flag = False
