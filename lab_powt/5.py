def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a*b
def dzielenie(a,b):
    return a/b

kalk = {'+': dodawanie, '-':odejmowanie,'*':mnożenie,'/':dzielenie}

x = kalk['*'](10,2)
print(x)
