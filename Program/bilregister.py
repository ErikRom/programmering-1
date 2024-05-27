class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand

    def set_color(self, new_color):
        '''
        Väljer en ny färg på bilen
        '''

    def set_mileage(self, new_mileage):
        '''
        Väljer ett nytt mileage
        '''
    def get_mileage(self):
        return self.mileage


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('Renault')
a_car.get_brand()
print(a_car.color)
the_mileage = a_car.get_mileage()
print(a_car.mileage)


b_car = Car('BMW', 'Grön', 1300)
b_car.get_brand()
b_car.set_brand('Mercedes')
b_car.get_brand()


c_car = Car('Ferarri', 'Cyan', '999')


d_car = Car('Porsche', 'Röd', '2000')


my_cars = [a_car, b_car, c_car, d_car]

for cars in my_cars:
    print(cars.brand, cars.color, cars.mileage)

val = input("Vad se märken, färger eller miltal (Skriv 'avsluta' för att avsluta): ")


if val == "märken":
    alfabetet = "abcdefghijklmnopqrstuvwxyz"
    for cars in my_cars:
        print(cars.brand)

if val == "färger":
    alfabetet = "abcdefghijklmnopqrstuvwxyz"
    for cars in my_cars:
        print(cars.color)

if val == "miltal":
    for cars in my_cars:
        print(cars.mileage)
#Början till "om du hinner" uppgiften
