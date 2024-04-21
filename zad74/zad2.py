import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r_values = np.linspace(0, 1, 1000)
t_values = np.linspace(0, 4 * np.pi, 1000)

r, t = np.meshgrid(r_values, t_values)

x = np.real(r * np.exp(1j * t))
y = np.imag(r * np.exp(1j * t))
z = np.imag(np.sqrt(r) * np.exp(1j * t / 2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='cividis')

ax.set_xlabel(r'$ℜ(re^{ıt})$')
ax.set_ylabel(r'$ℑ(re^{ıt})$')
ax.set_zlabel(r'$ℑ(√r exp(ıt/2))$')
ax.set_title(r'2. $S_c$')

plt.show()
