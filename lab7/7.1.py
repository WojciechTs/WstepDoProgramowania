import numpy as np
import random
pot2 = [ 2**(7-i) for i in range(8)]
wagi = np.array(pot2)
#licz = [random.randint(0,1) for i in range(8)]
#liczba_bin = np.array(licz)
liczba_bin = np.random.randint(low=0,high=2,size=(8))
dzies = wagi*liczba_bin
suma = dzies.sum()
print(suma)
