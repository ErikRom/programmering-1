number1 = int(input("tal 1: " ))
number2 = int(input("tal 2: " ))

x = list(range(number1, number2 + 1))

for i in x:
    if i % 2 != 0:
        x.remove(i)

print(x)
