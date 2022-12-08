def find(wartosc,lista):
    n=0
    indeks = []
    for i in lista:
        if i == wartosc:
            indeks.append(n)
            continue
        n+=1

    return indeks

print(find(3,[1,2,3,4,3]))
