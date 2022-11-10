zwierzeta = []
for i in range(5):
    x = input("Podaj nazwy zwierząt: ")
    zwierzeta.append(x)
zwierzeta.sort()
print(zwierzeta[0],zwierzeta[-1],zwierzeta[-2],zwierzeta[-3])
print(len(zwierzeta))