punkty = []
import random
i = 0
while i <= 15:
    x = random.uniform(0,50)
    x = round(x,2)
    punkty.append(x)
    i+=1

print(f"Największa ilość punktów: {max(punkty)}")
print(f"Najmniejsza ilość punktów: {min(punkty)}")

a = float(input("Podaj wybraną liczbe: "))
if a in punkty:
    print(punkty.index(a))
else:
    print("liczba nie występuje w liczbie")

"""suma = 0
for i in range(15):
    suma += punkty[i]"""
suma = sum(punkty)

srednia = suma / 15
print(srednia)
zdalo = []
niezdalo = []
for i in range(15):
        if punkty[i] > srednia:
            zdalo.append(punkty[i])
        if punkty[i] < srednia:
            niezdalo.append((punkty[i]))


print(f"{len(zdalo)} osób zdobyło punkty powyżej średniej")
print(f"{len(niezdalo)} osób zdobyło punkty poniżej średniej")
print("punkty powyżej średniej:")
print(zdalo)

print("punkty poniżej średniej:")
print(niezdalo)

