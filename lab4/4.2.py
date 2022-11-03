import random
x = int(input("Podaj liczbe elementow: "))
y = int(input("Podaj liczbe elementow: "))
zestaw_1 = []
for i in range(x):
    z = random.randint(1,10)
    zestaw_1.append(z)
print(zestaw_1)


zestaw_2 = []
for i in range(y):
    z = random.randint(5,15)
    zestaw_2.append(z)
print(zestaw_2)