import numpy as np
"""import matplotlib.pyplot as plt

x = np.arange(-4, 5, 0.25)
y = 5 * x**2 - 4 * x -1
plt.plot(x, y)
plt.show()"""

import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi,100)

plt.plot(x, np.sin(x))
plt.plot(x, 2*np.sin(x))
plt.plot(x, 2+np.sin(x))
plt.plot(x, np.sin(x/2))
plt.show()