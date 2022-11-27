# #modyfikowanie elementów na liscie
# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0]='ducati'
# print(motorcycles)

#dodawanie elemetów do listy

#umieszczenie elemenentu na końcu listy
# motorcycles=['honda','yamaha','suzuki']
# motorcycles.append('ducati')
# print(motorcycles)
#
# motorcycles = []
#
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
#
# print(motorcycles)

#Wstawianie elementów na listę

# motorcycles=['honda','yamaha','suzuki']
#
# motorcycles.insert(1,'ducati')
# print(motorcycles)

#Usuwanie elementów z listy

#usunięcie elementu z listy za pomocą polecenia del

# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
#
# del motorcycles[0]
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)

#Usunięcie z elementu za pomocą metody pop()

# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
#
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles=['honda','yamaha','suzuki']
# last_owned=motorcycles.pop()
# print("Ostatnio nabyty motocykl to " + last_owned.title())

#Usunięcie elementu z dowolnego miejsca na liście

# motorcycles=['honda','yamaha','suzuki']
# first_owned = motorcycles.pop(0)
# print("Mój pierwszy motocykl to : " + first_owned.title())

#Usunięcie elementu na podstawie wartości

# motorcycles=['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# motorcycles=['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# too_expensive='ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nMotocykl "+too_expensive.title()+" jest zbyt drogi dla mnie")

#3.4

# guest_lst=['Antoni Macierewicz', 'Twoja Stara', 'Marcin Stupka']
# print("Zapraszam na obiad " + guest_lst[0])
# print("Zapraszam na obiad " + guest_lst[1])
# print("Zapraszam na obiad " + guest_lst[2])

#3.5

# guest_lst=['Antoni Macierewicz', 'Twoja Stara', 'Marcin Stupka']
# print("Zapraszam na obiad " + guest_lst[0])
# print("Zapraszam na obiad " + guest_lst[1])
# print("Zapraszam na obiad " + guest_lst[2])
# print("Niestety " + guest_lst[2]+ " nie przyjdzie na obiad")
# guest_lst.remove("Marcin Stupka")
# guest_lst.append("Zenon Beznazwiska")
# print("Zapraszam na obiad " + guest_lst[0])
# print("Zapraszam na obiad " + guest_lst[1])
# print("Zapraszam na obiad " + guest_lst[2])

#3.6
#
# guest_lst=['Antoni Macierewicz', 'Twoja Stara', 'Marcin Stupka']
# print("Zapraszam na obiad " + guest_lst[0])
# print("Zapraszam na obiad " + guest_lst[1])
# print("Zapraszam na obiad " + guest_lst[2])
# print("Niestety " + guest_lst[2]+ " nie przyjdzie na obiad")
# guest_lst.remove("Marcin Stupka")
# guest_lst.append("Zenon Beznazwiska")
# print("Zapraszam na obiad " + guest_lst[0])
# print("Zapraszam na obiad " + guest_lst[1])
# print("Zapraszam na obiad " + guest_lst[2])
# print("Znaleziono większy stół w związku z tym zapraszam trzy kolejne osoby")
# guest_lst.insert(0,"Pan Pierwszy")
# guest_lst.insert(3,"Pan Środkowy")
# guest_lst.append("Pan Oostatni")
# print("Zapraszam na obiad " + guest_lst[0])
# print("Zapraszam na obiad " + guest_lst[1])
# print("Zapraszam na obiad " + guest_lst[2])
# print("Zapraszam na obiad " + guest_lst[3])
# print("Zapraszam na obiad " + guest_lst[4])
# print("Zapraszam na obiad " + guest_lst[5])

#3.7


guest_lst=['Antoni Macierewicz', 'Twoja Stara', 'Marcin Stupka']
print("Zapraszam na obiad " + guest_lst[0])
print("Zapraszam na obiad " + guest_lst[1])
print("Zapraszam na obiad " + guest_lst[2])
print("Niestety " + guest_lst[2]+ " nie przyjdzie na obiad")
guest_lst.remove("Marcin Stupka")
guest_lst.append("Zenon Beznazwiska")
print("Zapraszam na obiad " + guest_lst[0])
print("Zapraszam na obiad " + guest_lst[1])
print("Zapraszam na obiad " + guest_lst[2])
print("Znaleziono większy stół w związku z tym zapraszam trzy kolejne osoby")
guest_lst.insert(0,"Pan Pierwszy")
guest_lst.insert(3,"Pan Środkowy")
guest_lst.append("Pan Oostatni")
print("Zapraszam na obiad " + guest_lst[0])
print("Zapraszam na obiad " + guest_lst[1])
print("Zapraszam na obiad " + guest_lst[2])
print("Zapraszam na obiad " + guest_lst[3])
print("Zapraszam na obiad " + guest_lst[4])
print("Zapraszam na obiad " + guest_lst[5])
print("Niestety mogę zaprosić tylko dwie osoby")
popped_guest=guest_lst.pop()
print("Niestety wypierdalaj: "+ popped_guest)
popped_guest=guest_lst.pop()
print("Niestety wypierdalaj: "+ popped_guest)
popped_guest=guest_lst.pop()
print("Niestety wypierdalaj: "+ popped_guest)
popped_guest=guest_lst.pop()
print("Niestety wypierdalaj: "+ popped_guest)
print("Zapraszam na obiad panie:" + guest_lst[0])
print("Zapraszam na obiad panie:" + guest_lst[1])
del guest_lst[0]
del guest_lst[0]

print(guest_lst)