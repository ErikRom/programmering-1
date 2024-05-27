import time

minlista = []

val = 1

while val != "7":
    val = input("------------------------------------" "\nVad vill du göra? " "\n1. Titta på hela listan " "\n2. Titta på en specifik listposition " "\n3. Lägga till ett värde i listan " "\n4. Ta bort ett värde i listan" "\n5. Sortera listan " "\n6. Beräkna listans medelvärde " "\n7. Avsluta" "\n------------------------------------" "\n")
    
    if val == "1":
        print(minlista)
    if val == "2":
        titta = int(input("Vilken position vill du titta på? "))
        print([titta])
    if val == "3":
        tillägg = int(input("Vilket tal vill du lägga till? "))
        minlista.append(tillägg)
    if val == "4":
        tabort = int(input("Vilket indexnummer i listan vill du ta bort? "))
        minlista.pop(tabort)
    if val == "5":
        sortering = input("Baklänges eller Framlänges? ")
        if sortering == "Baklänges":
            minlista.sort(reverse=True)
            print(minlista)
        elif sortering == "Framlänges":
            print(sorted(minlista))
        else:
            print("Otillåtet val")
    if val == "6":
        print(sum(minlista)/len(minlista))
    if val == "7":
        print("Klart")
    time.sleep(0.4)
