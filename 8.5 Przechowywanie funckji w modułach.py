#IMPORT CAŁEGO MODUŁU
# import pizza
#
# pizza.make_pizza(40,'pepperoni')
# pizza.make_pizza(30,'pieczarki','zielona papryka')
"""nazwa_modułu.nazwa_funkcji()"""
#IMPORT OKREŚLONYCH FUNKCJI

"""

from nazwa_modułu import nazwa_funkcji
from nazwa_modułu import nazwa_funkcji_0, nazwa_funkcji_1, nazwa_funkcji_2

"""
#
# from pizza import make_pizza
# make_pizza(40,'pieczarki')
# make_pizza(30,'ser','szynka')

#UŻYCIE SŁOWA KLUCZOWEGO AS W CLU ZDEFINIOWANIA ALIASU FUNKCJI
"""from nazwa_modułu import nazwa_funkcji as alias"""
# from pizza import make_pizza as mp
#
# mp(40,'pepperoni')
# mp(30,'ser','szynka')

#UŻYCIE SŁOWA KLUCZOWEG AS W CELU ZDEFINIOWANIA ALIASU MODUŁU

"""impor nazwa_modułu as alias"""
# import pizza as p
# p.make_pizza(40,'pepperoni')
# p.make_pizza(30,'ser','szynka')

#IMPORT WSZYSTKICH FUNKCJI MODUŁU

# from pizza import *
# make_pizza(40,'pieczarki')
# make_pizza(30,'ser','szynka')

#NADAWANIE STYLU FUNKCJOM

"""
def nazwa_funkcji(parametr_0, parametr_1='wartość domyślna')
    'docstring'

nazwa_funkcji(wartość_0, parametr_1='wartość'

def nazwa_funkcji(
        parametr_0, parametr_1, parametr_2,
        parametr_3, parametr_4, parametr_5):
    tresć funkcji...
"""

#8.15
# import printing_functions
# unprinted_designs=['koza','gówno']
# completed_models=[]
# printing_functions.print_models(unprinted_designs,completed_models)
# printing_functions.show_completed_models(completed_models)
#8.16
# import my_function
# my_function.my_function('baretk','sławiński')
# from my_function import my_function
# my_function('andrzej','kaczmarek')
# from my_function import my_function as mf
# mf('Mf','doom')
# import my_function as mfs
# mfs.my_function('mf','soom')
# from my_function import *
# my_function('my','function')