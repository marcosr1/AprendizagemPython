import numpy as np
import matplotlib.pyplot as plt

P0 = 1000
r = 0.05
t = np.linspace(0, 50, 100)

P = P0 * np.exp(r * t)

plt.plot(t, P)
plt.xlabel('Tempo (anos)')
plt.ylabel('População')
plt.title('Modelo Exponencial de Crescimento Populacional') 
plt.show()


