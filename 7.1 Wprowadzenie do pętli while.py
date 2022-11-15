#PĘTLA WHILE W DZIAŁANIU

# current_number  = 1
# while current_number <= 5:
#     print(current_number)
#     current_number +=1

#UMOŻLIWIENIE UŻYTKOWNIKOWI PODJĘCIA DECYZJI O ZAKONCZENIU DZIAŁANIA PROGRAMU

# prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie."
# prompt +="\nNapisz 'koniec' aby zakończyć działanie programu."
# message=""
# while message != 'koniec':
#     message=input(prompt)
#     if message !='koniec':
#         print(message)

#UŻYCIE FLAGI

# prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie."
# prompt +="\nNapisz 'koniec' aby zakończyć działanie programu."
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'koniec':
#         active=False
#     else:
#         print(message)

#UŻYCIE POLECENIA BREAK DO OPUSZCZENIA PĘTLI

# prompt = "\nPodaj nazwy miast, które chciałbyś odwiedzić:"
# prompt += "\nGdy zakończysz podawanie miast, napisz 'koniec'"
#
# while True:
#     city = input(prompt)
#     if city =='koniec':
#         break
#     else:
#         print(f"Chciałbym odwiedzić {city.title()}")

#UŻYCIE POLECENIA CONTINUE W PĘTLI

# current_number=0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

#UNIKANIE PĘTLI DZIAŁJĄCEJ W NIESKOŃCZONOŚĆ
#
# x=1
# while x<=5:
#     print(x)
#     x+=1 #usuń te linie  i sprawdź

#7.4

# prompt = "\nPodaj dodatki do pizzy."
# prompt +="\nNapisz 'koniec' aby zakończyć działanie programu."
# message=""
# while message != 'koniec':
#     message=input(prompt)
#     if message !='koniec':
#         print(message.title())
#     else:
#         print("Twoja pizza już do Ciebie jedzie ")
#7.5
# age= int(input("Podaj swój wiek: "))
# if age < 3:
#     print("Twój bilet do kina jest bezpłatny")
# elif age >3 and age <12:
#     print("Twój bilet kosztuje 10 zł")
# elif age >12:
#     print("Twój bilet kosztuje 15 zł")

#7.6

# prompt = "\nPodaj dodatki do pizzy."
# prompt +="\nNapisz 'koniec' aby zakończyć działanie programu."

# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'koniec':
#         active=False
#     else:
#         print(message)


# while True:
#     toppings = input(prompt)
#     if toppings =='koniec':
#         break
#     else:
#         print(f"Chciałbym dodatek {toppings.title()}")


#7.7

# current_number  = 1
# while current_number <= 5:
#     print(current_number)
