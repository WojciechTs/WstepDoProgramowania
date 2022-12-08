import numpy as np
tab = np.zeros(shape=(3,3))
#tab[1:,:2] = 1
#tab[:,2:] = 1
#tab[:2,:] = 1
#tab[:2,:1]= 1
tab[:2,[0,2]] = 1
print(tab)