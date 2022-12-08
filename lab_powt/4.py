def znaki(slowo):
    znak = {}
    for i in slowo:
        if i not in znak.keys():
            znak[i] = 0
        if i in znak.keys():
            znak[i] += 1

    return znak
x = znaki("znaki napisu")
print(x)