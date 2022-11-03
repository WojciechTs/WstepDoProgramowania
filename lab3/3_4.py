x = int(input("Podaj liczbę nr 1: "))
y = int(input("Podaj liczbę nr 2: "))

if x > y:
    x,y = y,x

while x < y:
    if x % 2 == 1:
        x += 1
        continue
    print(x)
    x+=1
