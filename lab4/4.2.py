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

z = int(input(" Podaj liczbe: "))
"""i = 0
while i <= x or i <= y:
    if z == zestaw_1[i]:
        print("Liczba z zestawu 1")
        break

    if z == zestaw_2[i]:
        print("Liczba z zestawu 2")
        break
        
    i+=1
"""
if z in zestaw_1:
    print("Liczba z zestawu 1")
if z in zestaw_2:
    print("Liczba z zestawu 2")
if z not in zestaw_1 and z not in zestaw_2:
    print("Nie ma takiej liczby w obu zestawach")

"""if z in zestaw_1:
    print("Liczba z zestawu 1")
elif z in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")"""

zestaw_1_2 = zestaw_1 + zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)