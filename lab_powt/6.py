import numpy as np
macierz = np.zeros((5,5))
print(macierz)
def jedynki():
    macierz[:1,]=1
    macierz[4:, ] = 1
    macierz[:,:1 ] = 1
    macierz[:, 4:] = 1

def zera():
        macierz[:1, ] = 0
        macierz[4:, ] = 0
        macierz[:, :1] = 0
        macierz[:, 4:] = 0
jedynki()
print(macierz)
zera()
print(macierz)