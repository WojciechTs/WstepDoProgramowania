import numpy as np
macierz = np.random.randint(low=0,high=11,size=(5,5))
print(macierz)
print(macierz.min(axis = 1))
print(macierz.max(axis = 0))
print(macierz.sum(axis=1))