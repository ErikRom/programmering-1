number1 = 1
number2 = 2

print(number1)
print(number2)
while True:
    number = number1+number2
    number1 = number2
    number2 = number
    if number%2 == 0:
        suma += number
        if number > 4000000:
        break
    else:
        print(number)
        continue
