# SPRAWDZANIE POD KĄTEM WARTOŚĆI SPECJALNYCH

# requested_toppings = ['pieczarki','boczek','podwójny ser']
#
# for requested_toppings in requested_toppings:
#     if requested_toppings == 'boczek':
#         print("Przepraszamy, ale obecnie nie mamy boczku.")
#     else:
#         print("Dodaję " + requested_toppings + ".")
# print("\nTwoja pizza jest już gotowa!")
#

#SPRAWDZANIE CZY LISTA NIE JEST PUSTA

# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Dodaję "+requested_topping+ ".")
#     print("\nTwoja pizza jest juz gotowa.")
# else:
#     print("Czy jesteś pewnien, że chcesz pizze bez dodatkow? ")

#UŻYCUE WIELU LIST
#
# avalible_toppings= ['pieczarki','oliwki','boczek','pepperoni','ananas','podwójny ser']
# requested_toppings=['pieczarki','frytki','podwójny ser']
#
# for requested_topping in requested_toppings:
#     if requested_topping in avalible_toppings:
#         print("Dodaję "+ requested_topping+ '.')
#     else:
#         print("Przepraszamy ale obecnie nie mamy dodatku "+requested_topping + '.')
#
# print("\nTwoja pizza jest gotowa.")

#5.8
#
# user_lst= ['user1','user2','user3','user4','admin']
# for user in user_lst:
#     if user == 'admin':
#         print("Witaj admin, co u ciebie!")
#     else:
#         print("Witaj " + user)

#5.9
# #
# user_lst= ['user1','user2','user3','user4','admin'] # Po usunięciu elementów z listy kod wykona się i poda else
# if user_lst:
#     for user in user_lst:
#         if user == 'admin':
#             print("Witaj admin, co u ciebie!")
#         else:
#             print("Witaj " + user)
# else:
#     print("Lista jest pusta!")

# 5.10
# current_users = ['user1','user2','user3','user4','admin']
# current_users_upper=[user.upper() for user in current_users ]
# new_users =  ['user5','user6','user7','user8','admin']
# new_users_upper=[user.upper() for user in new_users]
# for user in new_users_upper:
#     if user in current_users_upper:
#         print("Ta nazwa jest zajęta")
#     else:
#         print("Ta nazwa jest wolna")
# print(new_users_upper)
# print(current_users_upper)

#5.11

# number_lst=['1','2','3','4','5','6','7','8','9']
# for number in number_lst:
#     if number == '1' :
#         print('1st')
#     elif number == '2':
#         print('2nd')
#     elif number == '3':
#         print('3rd')
#     elif number == '4'and'5'and'6'and'7'and'8'and'9':
#         print('4th\n5th\n6th\n7th\n8th\n9th')
