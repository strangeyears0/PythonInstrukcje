# PROSTY PRZYKŁAD

# cars= ['audi','bmw','subaru','toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

#Test warunkowy

#sprawdzenie równości
#
# car='bmw'
# print(car=='bmw')
#
# car='audi'
# print(car=='bmw')

#ignorowanie wielkości liter podczas sprawdzania równości

# car='Audi'
# print(car=='audi')
#
# car='Audi'
# print(car.lower()=='audi')
# car='Audi'
# print(car.lower()=='audi')
# print(car)


#sprawdzanie nierówności

# requested_topping = 'pieczarki'
# if requested_topping != 'anchois':
#     print("Poproszę o anchois!")

#porównania liczbowe

# age=18
# print(age==18)
#
# answer=17
# if answer != 42:
#     print("To nie jest prawidłowa odpowiedź try again")

# age=19
# print(age<21)
# print(age<=21)
# print(age>21)
# print(age>=21)

#użycie słowa kluczowego and do sprawdzania wielu warunków

# age_0 = 22
# age_1 = 18
# print(age_0 >=21 and age_1 >=21)
# age_0 = 22
# age_1 = 21
# print(age_0 >=21 and age_1 >=21)

#Użycie słowa kluczowego OR  do sprawdzania wielu warunków
#
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >=21)
# age_0 = 18
# print(age_0 >= 21 or age_1 >=21)

#sprawdzanie czy wartość znajduje się na liście

# requested_toppings = ['pieczarki','cebula','ananas']
# print('pieczarki' in requested_toppings)
# print('pepperoni' in requested_toppings)

#sprawdzanie czy wartośc nie znaduje sie na liscie
#
# banned_users = ['andrzej','karolina','dawid']
# user='maria'
#
# if user not in banned_users:
#     print(user.title() + ", możesz opublikować odpowiedź.")

#wYRAŻENIE boolowskie

# game_active= True
# can_edit = False
#


#5.1
# car='subaru'
# print("czy car == 'subaru'? ")
# print(car=='subaru')
#
# print("Czy car ='audi?'")
# print(car == 'audi')
#
# car= 'BMW'
# print("car == 'bmw'")
# print(car=='bmw')
# print(car=='BMW')

#5.2
# a="Adam"
# print('Adam'=='Adam')
# print('Adam'=='adam')
# print('adam'==a.lower())
# print('Adam'==a.lower())
# x=1
# y=2
# print("------------")
# print(x>y)
# print(x<y)
# print(x<=y)
# print(x>=y)
# print(x==y)
# print("-----------")
# print(x>3 and y >3)
# print(x>2 or y>=2)
# print("----------")
# lst_1=['Marta','Koto','Królik']
# print('Marta' in lst_1)
# print('Pjes' in lst_1)
# print("----------")
# lst_2=['Marta','Koto','Królik']
# user='Pjes'
#
# if user not in lst_2:
#     print('Pjes nie znajduje się na liście lst_2')
#     print(lst_2)
#     print(lst_2)

# POLECENIE IF

#Proste polecenia IF
#
# age= 19
# if age >= 18:
#     print("Możesz wziąć udział w głosowaniu")
#     print("Czy zarejestrowałeś się już, aby móc głosować?")

#POLECENIA IF else
#
# age= 17
# if age >= 18:
#     print("Możesz wziąć udział w głosowaniu")
#     print("Czy zarejestrowałeś się już, aby móc głosować?")
# else:
#     print("Przykro nam ale jesteś zbyty młody aby głosować")
#     print("Możesz się zarejestrować po ukończeniu 18 lat")

#łańcuch if-elif-else

# age= 12
#
# if age < 4:
#     print("Cena biletu wstępu wynosi 0 zł.")
# elif age < 18:
#     print("Cena biletu wstępu wynosi 5zł.")
# else:
#     print("Cena biletu wstępu wnosi 10zł.")


# age= 12
#
# if age < 4:
#     price=0
# elif age < 18:
#     price = 5
# else:
#     price=10
# print("Cena biletu wynosi " + str(price) + " zł.")

#Użycie wielu bloków elif

# age= 64
#
# if age < 4:
#     price=0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price=10
# else:
#     price=5
# print("Cena biletu wynosi " + str(price) + " zł.")


#Pominięcie bloku else

# age= 64
#
# if age < 4:
#     price=0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price=10
# elif age >= 65:
#     price=5
# print("Cena biletu wynosi " + str(price) + " zł.")


# #Sprawdzanie wielu warunków
# requested_toppings = ['pieczarki','podwójny ser']
# if 'pieczarki' in requested_toppings:
#     print("Dodaj pieczarki.")
# if 'pepperoni' in requested_toppings:
#     print("Dodaję pepperoni.")
# if 'podwójny ser' in requested_toppings:
#     print("Dodaje podwójny ser.")
#
# print("\nTwoja pizza jest już gotowa")


#5.3
#
# alien_color = ['zielony','zolty','czerwony']
# if 'zielony' in alien_color:
#     print("Zarobiłeś 5 pkt.")

#5.4

# alien_color=['zielony','zolty','czerwony']
# if 'zielony' in alien_color:
#     print("Zarobiłeś 5 pkt za zestrzelenie obcego")
# else:
#     print("Zarobiłeś 10 pkt")
#
# alien_color=['zielony','zolty','czerwony']
# if not 'zielony' in alien_color:
#     print("Zarobiłeś 5 pkt za zestrzelenie obcego")
# else:
#     print("Zarobiłeś 10 pkt")

#5.5
#
# alien_color=['zielony','zolty','czerwony']
#
# if not'zielony' in alien_color:
#     print('Zarobiłeś 5 pkt')
# elif not 'zolty' in alien_color:
#     print("zarobiłeś 10 pkt")
# else:
#     print("Zarobiłeś 15 pkt")

#5.6

# age = 7
#
# if age < 2 :
#     print("Jesteś niemowlęciem.")
# if age > 2 and age < 4:
#     print("Jesteś dzieckiem które uczy się chodzić")
# if age > 4 and age < 13:
#     print("Jesteś dzieckiem")
# if age > 13 and age < 20:
#     print("Jesteś nastolatkiem")
# if age > 20 and age < 65:
#     print("Jesteś dorosły")
# if age > 65 :
#     print("jesteś starym dziadem")

#5.7
#
# favorite_fruits = ['appple','banana','mango']
# if 'appple' in favorite_fruits:
#     print("Lubisz jabłka")
# if 'gówno' in favorite_fruits:
#     print("\n")
# if 'banana' in favorite_fruits:
#     print("Lubisz banany")
# if 'swinia' in favorite_fruits:
#     print("\n")
# if 'mango' in favorite_fruits:
#     print("Lubisz mango")
#

