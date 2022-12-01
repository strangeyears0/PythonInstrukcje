#IMPORT POJEDYNCZEJ KLASY

# from car import Car
# my_new_car = Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#PRZECHOWYWANIE WIELU KLAS W MODULE

# from car import ElectricCar
#
# my_tesla = ElectricCar('tesla','roadster',2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

#IMPORT WIELU KLAS Z MODUŁU

# from car import Car, ElectricCar
# my_beetle = Car('volkswagen','beetle',2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())

#IMPORT CAŁEGO MODUŁU

# import car
#
# my_beetle = car.Car('wolksvagen','beetle',2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla','roadster',2019)
# print(my_tesla.get_descriptive_name())


#IMPORT WSZYSTKICH KLAS Z MODUŁU
# from car import *
#NIEZALECANE

#IMPORT MODUŁU W MODULE

# from car import Car
# from electric_car import ElectricCar
#
# my_beetle = Car('volkswagen','beetle',2015)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla','roadster',2019)
# print(my_tesla.get_descriptive_name())
#

#9.10
#
# from restaurant import Restaurant
# my_restaurant = Restaurant('U Bartka','Jadłodajnia')
# print(my_restaurant.describe_restaurant())

#9.11


# from User import Admin
#
# admin = Admin('User','Name','Username','u@g.com','polon')
# print(admin.privileges.show_privileges())

#9.12


# from adminandprivileges import *
#
# admin = Admin('User','Name','Username','u@g.com','polon')
# print(admin.privileges.show_privileges())
# print(admin.describe_user())