x = int(input("Podaj liczbę nr 1: "))
y = int(input("Podaj liczbę nr 2: "))

if x > y:
    x,y = y,x

while x < y:
    print(x)
    x += 1
else:
    print(y)
