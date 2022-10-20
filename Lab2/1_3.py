print("""Jaką operację chcesz wykonać?
    1) dodawanie
    2) odejmowanie
    3) mnożenie
    4) dzielenie
    5) potęgowanie""")
y = int(input("Wpisz numer operacji: "))
z1 = int(input("Podaj argument 1: "))
z2 = int(input("Podaj argument 2: "))
if y == 1:
    wynik = z1 + z2
elif y == 2:
    wynik = z1 - z2
elif y == 3:
    wynik = z1 * z2
elif y == 4 and z2 != 0:
    wynik = z1 / z2
elif y == 4 and z2 == 0:
    wynik = "Nie wolno dzielic przez 0"
elif y == 5:
    wynik = z1 ** z2
else:
    wynik = "Operacja poza zakresu"

print (f"Wynik: {wynik}")


