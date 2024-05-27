import random

"""godispåsar = random.randint(1, 11)

arg = random.randint(1, 2)

if arg == 1:
    arg = 1
if arg == 2:
    arg = 5

bus = 10 - godispåsar - 1

poäng = godispåsar*2 - bus - arg


def resultat():
    print("Antal grannar besökta: 10" f"\nAntal godispåsar: {godispåsar}" f"\nAntal genomförda bus: {bus + 1}" f"\nTotal poäng: {poäng} (Av maximalt 20)")

resultat()"""

antal_besök = 0
poäng = 0
antal_godis = 0
antal_bus = 0

while antal_besök < 9:
    tal = random.randint(1,2)
    if tal == 1:
        poäng += 2
        antal_godis += 1
    else:
        poäng -= 1
        antal_bus += 1
    antal_besök += 1




print(f"Antal grannar besökta: {antal_besök}")
print(f"Antal godispåsar: {antal_godis}")
print(f"Antal genomförda bus: {antal_bus}")
print(f"Total poäng: {poäng} (av maximalt 20)")
