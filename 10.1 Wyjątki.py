#OBSŁUGIWANIE WYJĄTKU ZERODIVISIONERROR
#print(5/0)


#UŻYWANIE BLOKU TRY-EXCEPT

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Nie można dzielić przez zero!")

#UŻYWANIE WYJĄTKÓW W CELU UNIKNIĘCIA AWARII PROGRAMU

# print("Podaj dwie liczby które zostaną podzielone.")
# print("Wpisz 'q' aby zakończyć działanie programu.")
#
# while True:
#     first_number = input("\nPierwsza liczba: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nDruga liczba: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero!")
#     else:
#         print(answer)

#OBSŁUGA WYJĄTKU FILENOTFOUNDERROR
from importlib.resources import contents

# filename = 'alice1.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = f"Przepraszamy ale plik {filename} nie istnieje."
#     print(msg)


#ANALIZA TEKSTU

# filename = 'alice'
#
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = f"Przepraszamy ale plik {filename} nie istnieje."
#     print(msg)
# else:
#     #obliczanie liczby słów w PLIKU
#     words = contents.split()
#     num_words = len(words)
#     print(f"Plik {filename} zawiera {num_words} słów.")

#PRACA Z WIELOMA PLIKAMI
#
# def count_words(filename):
#     """Obliczanie przybliżonej liczby słow w danym pliku."""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = f"Przepraszamy ale plik {filename} nie istnieje."
#         print(msg)
#     else:
#         #obliczanie liczby słów w PLIKU
#         words = contents.split()
#         num_words = len(words)
#         print(f"Plik {filename} zawiera {num_words} słów.")
# # filename = 'alice'
# # count_words(filename)
#
# filenames = ['alice','pi_digits','what','dontexist']
# for filename in filenames:
#     count_words(filename)


#CICHE NIEPOWODZENIE

# def count_words(filename):
#     """Obliczanie przybliżonej liczby słow w danym pliku."""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         pass
#     else:
#         #obliczanie liczby słów w PLIKU
#         words = contents.split()
#         num_words = len(words)
#         print(f"Plik {filename} zawiera {num_words} słów.")
# # filename = 'alice'
# # count_words(filename)
#
# filenames = ['alice','pi_digits','what','dontexist']
# for filename in filenames:
#     count_words(filename)

#10.6

# try:
#     first_number = input("Podaj pierwszą liczbę :")
#     second_number  = input("Podaj drugą liczbę :")
#
#     first_number = int(first_number)
#     second_number = int(second_number)
# except:
#     print("Podaj liczbę nie napis")
#     quit()
# print("Dodawanie liczb...")
# gross = first_number + second_number
# print(f"Suma liczb {first_number} i {second_number} = {gross}")

#10.7

# while True:
#     try:
#         first_number = input("Podaj pierwszą liczbę :")
#         second_number  = input("Podaj drugą liczbę :")
#
#         first_number = int(first_number)
#         second_number = int(second_number)
#     except:
#         print("Podaj liczbę nie napis")
#     else:
#         print("Dodawanie liczb...")
#         gross = first_number + second_number
#         print(f"Suma liczb {first_number} i {second_number} = {gross}")


#10.8 , #10.9
#
#
# file_names = ['cats','dogs']
#
# def read_file(file_name):
#     try:
#             with open(file_name) as f_obj:
#                 contents = f_obj.read()
#                 print(contents)
#     except FileNotFoundError:
#             pass
# for file_name in file_names:
#     read_file(file_name)


#10.10


#
# filename = '145-0.txt'
#
# try:
#     with open(filename,errors='ignore') as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = f"Przepraszamy ale plik {filename} nie istnieje."
#     print(msg)
# else:
#     #obliczanie liczby słów w PLIKU
#     words = contents.split()
#     wordsthe= words.count('the')
#     print(f"Słowo the występuje {wordsthe} razy")
#     num_words = len(words)
#     print(f"Plik {filename} zawiera {num_words} słów.")