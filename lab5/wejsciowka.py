x = []

while len(x) <=5:
#for i in range(5):
    y = int(input("Podaj licze do listy: "))
    if y%2==0:
        x.append(y)

print(x)