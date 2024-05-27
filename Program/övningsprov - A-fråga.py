"""ditt_ord = input("ditt ord: ")

def rle():
    for i in ditt_ord:
        if ditt_ord[i] == ditt_ord[i+1]:
            antal_bokstäver += 1
            
    print(antal_bokstäver + i)
    


def convert(string):
    listposition = 0
    antal_bokstäver = 1
    
    lista = []
    lista[:0] = string
    return lista

print(convert(ditt_ord))
rle()"""

def rle(sträng):
    sträng += "."

    antal = 1
    for i in range(len(sträng)-1):
        if sträng[i] == sträng[i+1]:
            antal += 1
        else:
            if antal > 1:
                print(f"{antal}{sträng[i]}", end = "")
            else:
                print(f"{sträng[i]}", end = "")
            antal = 1

rle("kkkaaakkajfjd")
