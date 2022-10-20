x = input("Podaj literkę: ")
if x >= 'a' and x <= 'z':
    y = x.upper()
elif x >= 'A' and x <= 'Z':
    y = x.lower()
else:
    y = "nie podano litere"

print(y)