def potega(lista1,lista2):
    lista = []
    if len(lista1) == len(lista2):

        for i in range(len(lista1)):
            x = lista1[i] ** lista2[i]
            lista.append(x)
        return lista
    if len(lista1) != len(lista2):
        print("nie równe długości list")
        return
x1 = [2,2,2,2]
x2 = [1,2,3]
y = potega(x1,x2)
print(y)