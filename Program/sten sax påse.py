spelare1 = str(input("Spelare 1 - sten(0)/sax(1)/påse(2): "))
spelare2 = str(input("Spelare 2 - sten(0)/sax(1)/påse(2): "))

"sten" >= "sax"
"påse" <= "sax"
"påse" >= "sten"

vinnare = max(spelare1, spelare2)

print(vinnare)
