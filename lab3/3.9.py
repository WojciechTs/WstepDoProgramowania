x = int(input("Podaj liczbe wierszy: "))
x1 = x
#y = int(input("Podaj liczbe gwiadek: "))
s = ""
znak = "* "
znak1 = "*"
sp = " "
i = 1
j = 0
"""for i in range(x): wersja łatwa
        s += znak1
        print(s)
"""
for i in range(i,x+1):
    z = x1 - i
    s = sp * z + znak * i
    print(s)
    s = ""

