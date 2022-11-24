def oblicz(x,y):
    roz = x -y
    sum = x + y
    return roz,sum

a = input("Podaj x: ")
b = input("Podaj y: ")

w = oblicz(12.34,45.234)
print(w[0],w[1])


a,b = oblicz(56,34.78)
print(a,b)