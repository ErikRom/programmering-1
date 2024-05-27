import time

minlista = []

def tittapålista():
    print("------------------------------" f"\nDin lista --> {minlista}")
def tittapåposition():
    try:
        titta = int(input("------------------------------" "\nVilken position vill du titta på: "))
        print(f"Din lista --> {minlista[titta]}")
    except (ValueError, IndexError):
        print("Listposition existerar inte")
def läggatill():
    try:
        val = input("------------------------------" "\nVill du lägga till ett(e) eller många(m) tal: ")
        if val == "e":
            lägga = int(input("Vilket värde vill du lägga till: "))
            minlista.append(lägga)
            print(f"Lagt till --> {lägga}")
        elif val == "m":
            lägga1 = int(input("Från vilket värde vill du lägga till tal: "))
            lägga2 = int(input("Till vilket värde vill du lägga till tal: "))
            y = list(range(lägga1, lägga2+1))
            minlista.append(y)
            lägga3 = print(f"Lade till talen {lägga1} till {lägga2}")
        else:
            print("Skriv m eller e")
    except (ValueError, IndexError):
        print("Försök igen")
def tabort():
    try:
        bort = int(input("------------------------------" "\nVilken listposition vill du ta bort: "))
        minlista.pop(bort)
        print(f"Borttaget värde --> {bort}")
    except (ValueError, IndexError):
        print("Listposition existerar inte")
def sortera():
    try:
        minlista1 = sorted(minlista)
        håll = input("------------------------------" "\nBaklänges(b) eller Framlänges(f): ")
        if håll == "f":
            print(f"--> {minlista1}")
        elif håll == "b":
            print(f"--> {minlista1[::-1]}")
        else:
            print("Skriv f eller b")
    except (ValueError, IndexError):
        print("Försök igen")
def medel():
        print("------------------------------" f"\nMedelvärde --> {sum(minlista)/len(minlista)}")


while True:
    time.sleep(0.4)
    print("------------------------------\n1. Titta på hela listan" "\n2. Titta på en specifik listposition" "\n3. Lägga till ett värde" "\n4. Ta bort ett värde i listan" "\n5. Sortera listan" "\n6. Beräkna listans medelvärde" "\n7. Avsluta" "\n------------------------------")
    x = input("Vad vill du göra --> ")
    if x == "1":
        tittapålista()
    if x == "2":
        tittapåposition()
    if x == "3":
        läggatill()
    if x == "4":
        tabort()
    if x == "5":
        sortera()
    if x == "6":
        medel()
    if x == "7":
        print("--> Avslutat")
        break
