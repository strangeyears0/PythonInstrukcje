#PRZEKAZYWANIE LISTY
# def greet_users(names):
#     """Wyświetla proste powitanie każdemu użytkownikowi z listy"""
#     for name in names:
#         msg = f"Witaj {name.title()} !"
#         print(msg)
# usernames= ['halina','tymek','marzena']
# greet_users(usernames)
#MODYFIKOWANIE LISTY W funkcji

#Rozpoczynamy od pewnych projektow ktore maja byc wydrukowane
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []

#symulujemy wydruk dopóki zostal jakis na liscie
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Wydruk modelu : {current_design}")
#     completed_models.append(current_design)
# #wyświetlanie wszystkich wydrukowanych modeli
# print("\nWydrukowane zostały następujące modele:")
# for completed_model in completed_models:
#     print(completed_model)
            #REORGANIZACJA

# def print_models(unprinted_designs, completed_models):
#     """Symulujemy wydruk poszczególnych projektów dopóki został jakikolwiek projekt na liscie.
#     Każdy wydrukowany model zostaje przeniesiony na listę completed_models"""
#
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         #symulacja wydruki 3d na podstawie modelu
#         print(f"Wydruk modelu: "+current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Wyświetla wszystkie modele które zostały wydrukowane."""
#     print("\nWydrukowane zostały następujące modele: ")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


#UNIEMOZLIWANIE MODYFIKOWANIA LISTY PRZEZ FUNKCJĘ

# nazwa_funkcji(nazwa_listy[:])
# print_models(unprinted_designs[:],completed_models)


#8.9

# magicians=['MagicznyAndrzej','CzarownicaMonika','Paprodziad']
# def show_magicians(names):
#     """Pokazuje po kolei imiona z listy"""
#     for name in magicians:
#         print(name)
# show_magicians(magicians)

#8.10
# def show_magicians(magicians):
#     """Pokazuje po kolei imiona z listy"""
#     for magician in magicians:
#         print(magician)
# def make_great(magicians):
#     new_list=[]
#     for magician in magicians:
#         new_list.append("Doskonały " +magician.title()  )
#     return new_list
# magicians=['MagicznyAndrzej','CzarownicaMonika','Paprodziad']
# new_list=make_great(magicians[:])
# show_magicians(magicians)
# show_magicians(new_list)
#8.11

# def show_magicians(magicians):
#     """Pokazuje po kolei imiona z listy"""
#     for magician in magicians:
#         print(magician)
# def make_great(magicians):
#     new_list=[]
#     for magician in magicians:
#         new_list.append("Doskonały " +magician.title()  )
#     return new_list
# magicians=['MagicznyAndrzej','CzarownicaMonika','Paprodziad']
# new_list=make_great(magicians[:])
# show_magicians(magicians)
# show_magicians(new_list)