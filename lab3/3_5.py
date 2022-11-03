n = int(input("Podaj liczbe studentów: "))
suma = 0
i = 1;
while 0 == 0:
    punkty = int(input(f"Podaj punkty studenta {i}: "))
    if punkty < 0 or punkty > 100:
        print("Poza przedziału")
        continue

    suma += punkty

    if i == n: break
    i += 1
srednia = suma/n
print(f"Średnia = {srednia}")






















