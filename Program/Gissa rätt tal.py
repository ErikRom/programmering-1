import random as rand

slumptal=rand.randint(1,10)

ditt_tal = 0

while ditt_tal != slumptal:

    ditt_tal = int(input("Gissa på ett tal mellan 1-10: "))
    if slumptal != ditt_tal:
        print("Fel")
        print(" ")
    
print("Du gissade rätt!")
