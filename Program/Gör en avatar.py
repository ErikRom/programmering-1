namn = input("Välj ett namn till din avatar: ")

print(" ")

villkor = 1
while villkor!=0:
    färg = str(input("Välj en av färg till din avatar (blå/röd/gul): "))
    if färg in ["blå", "röd", "gul"]:
        villkor = 0
    else : print("Ogiltig färg")
    
while villkor != 1:
    pronomen = str(input("Välj en pronomen för din avatar (man/kvinna/hen): "))
    if pronomen in ["man", "kvinna", "hen"]:
        villkor = 1
    else : print("Otillåtet pronomen")

while villkor !=0:
    styrka = int(input("Välj hur stark din avatar ska vara (1-10): "))
    if styrka in range(1, 11):
        villkor = 0
    else : print("Otillåtet värde")

print("Resultat")
print(" ")
print(f"Namn: {namn} ({pronomen})")
print(len(f"Namn: {namn}, {pronomen}")*"-")
print(f"Färg: {färg}")
print(len(f"Färg: {färg}")*"-")
print(f"Styrka: {styrka}")
