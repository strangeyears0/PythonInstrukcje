from random import randint


class Die():
    """Klasa Kostki"""
    def __init__(self, sides=6):
        """inicjalizacja atrybutu kostki"""
        self.sides = sides

    def roll_die(self):
        """Symulacja rzutu kostką"""
        return randint(1, self.sides)

d6 = Die()

results = []

for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of 6 sided die: ")
print(results)

d10 = Die(sides=10)

results = []

for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("10 rolls of 10 sided die: ")
print(results)

d20 = Die(sides=20)

results = []

for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("10 rolls of 20 sided die: ")
print(results)