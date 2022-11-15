# ITERACJA PRZEZ WSZYSTKIE PARY KLUCZ WARTOŚĆ
#
# user_0 = {
#     'username':'jkowalski',
#     'first':'jan',
#     'last':'kowalski',
# }
#
# for key,value in user_0.items():
#     print("\nKlucz: " + key)
#     print("\nWartość: " + value)

# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
#
# for name, lang in fav_lang.items():
#     print("Ulubiony język programowania użytkownika " + name.title() + " to " + lang.title() + "." )

#ITERAACJA PRZEZ WSZYSTKIE KLUCZE SŁOWNIKA

# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
#
# for name in fav_lang.keys():
#     print(name.title())
#
# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
#
# friends =['papiesz','sara']
# for name in fav_lang.keys():
#     print(name.title())
#     if name in friends:
#         print("Witaj, " + name.title() + " Widzę że twoim ulubionym językiem programownia jest " +
#         fav_lang[name].title())

# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
# if 'elzbieta' not in fav_lang.keys():
#     print("Zapraszam cię stara kurwo do ankiety")

# ITERACJA PRZEZ UPORZĄDKOWANIE SŁOWNIKA


# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
#
# for name in sorted(fav_lang.keys()):
#     print((name.title()) + " dzięki za udział w ankiecie.")


#ITERACJA PRZEZ WSZYSTKIE WARTOŚCI SŁOWNIKA
#
# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
#
# # print("W ankiecie zostaly wymienione nastepujace jezyki programowania: ")
# # for lang in fav_lang.values():
# #     print(lang.title())
#
# print("W ankiecie zostaly wymienione nastepujace jezyki programowania: ")
# for lang in set(fav_lang.values()): #zbiór
#     print(lang.title())
#
#


#6.4
#
# glosariusz={
#     'print':'\ndrukuj',
#     'if': '\njeżeli',
#     'while': '\ndopóki',
#     'and': '\ni',
#     'true': '\nprawda',
#     'false': '\nfałsz',
#     'title': '\ntytuł',
#     'set': '\nzbiór',
#     'keys': '\nklucze',
#     'values': '\nwartości',
# }
#
# for key,value in glosariusz.items():
#     print(f"{key.title()} oznacza w języku python: {value.title()}" )

#6.5

# rivers = {
#     'nil':'egipt',
#     'wisła':'polska',
#     'ganges':'indie'
# }
#
# for river,capitol in rivers.items():
#     print(f"{river.title()} przepływa prez {capitol.title()}")
# for river in rivers.keys():
#     print(river.title())
# for capitol in rivers.values():
#     print(capitol.title())

#6.6

# fav_lang = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'papiesz':'python',
# }
# ankieta_lst= ['janek','papiesz','grzegorz']
#
# for name in fav_lang.keys():
#     print(name.title())
#     if name in ankieta_lst:
#         print(f"Zachęcam cię {name.title()} do wzięcia udziału w ankiecie")