import numpy as np
import matplotlib.pyplot as plt

g = -9.81
t = np.linspace(0, 5, 100)

s = 0 + 0.5 * g * t**2

plt.plot(t, s)
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.title('Queda Livre de um Objeto')
plt.show()