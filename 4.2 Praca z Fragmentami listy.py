# Wycinek listy
#
# players=['karol','martyna','michał','florian','ela']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

#Iteracja przez wycinek

# players=['karol','martyna','michał','florian','ela']
# print("Oto trzech pierwszych graczy naszej drużyny:")
# for player in players[:3]:
#     print(player.title())

#Kopiowanie listy

# my_foods=['pizza','falafel','ciasto z marchwi']
# friend_foods=my_foods[:]
#
# my_foods.append('canollo')
# friend_foods.append('gówno')
#
# print("Moje ulubione potrawy to:")
# print(my_foods)
# print("\nUlubione potrawy mojego przyjaciela to:")
# print(friend_foods)

#4.10
#
# players=['karol','martyna','michał','florian','ela']
# print("Pierwsze trzy elementy listy to:"+ str(players[0:3]))
# print("Trzy elementyw środku to:"+ str(players[1:4]))
# print("Trzy ostatnie elementy to:" + str(players[2:]))


# #4.11
# pizzas = ['margaritta', 'neapolitanska', 'verona']
# friend_pizzas = pizzas[:]
# pizzas.append('wege')
# friend_pizzas.append('miesna')
# for pizza in pizzas:
#     print("Moja ulubiona pizza to :" + pizza)
# for pizza in friend_pizzas:
#     print("Mojego przyjaciela ulubione pizze to:"+ pizza)

#4.12

# my_foods=['pizza','falafel','ciasto z marchwi']
# friend_foods=my_foods[:]
#
# my_foods.append('canollo')
# friend_foods.append('gówno')
#
# for food in my_foods:
#     print(food)
# for food in friend_foods:
#     print(food)