"""x = int(input("Podaj wiek: "))
if x < 4:
    print("wstęp jest bezpłatny")
elif x <= 18:
    print("bilet kosztuje 10zł")
else:
    print("bilet kosztuje 20zł")
"""

x = int(input("Podaj wiek: "))
if x < 4:
    y = 0
elif x <= 18:
    y = 10
else:
    y = 20
print("bilet kosztuje",y,"zł")