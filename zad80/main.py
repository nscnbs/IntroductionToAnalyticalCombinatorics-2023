import matplotlib.pyplot as plt
import numpy as np

def f1(z): return np.abs(z)
def f2(z): return np.abs(z**2)
def f3(z): return np.abs(1 / (2 - np.exp(z)))
def f4(z): return np.abs(1 / ((1-z) * (1-z/2) * (1-z/3)))
def f5(z): return np.abs((1+z+z**2) / (1-z-z**2-z**3))
def f6(z): return np.abs((np.exp(-z)) / (2 - np.exp(z)))
def f7(z): return np.abs(np.sqrt(1 - 4*z))

# Tworzenie siatki punktów zespolonych
x = np.linspace(-20, 20, 1000)
y = np.linspace(-20, 20, 1000)
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

functions = [f1, f2, f3, f4, f5, f6, f7]
functions_titles = [
    '1. f(z) = |z|',
    '2. f(z) = |z^2|',
    '3. f(z) = 1 / (2 - e^(z))',
    '4. f(z) = 1 / ((1 - z)(1 - z/2)(1 - z/3))',
    '5. f(z) = (1 + z + z^2) / (1 - z - z^2 - z^3)',
    '6. f(z) = e^(-z) / 2 - e^z',
    '7. f(z) = √(1 - 4z)'
]

for i in range(7):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, np.abs(functions[i](Z)), cmap='cividis')
    ax.set_title(functions_titles[i])
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_zlabel('|f(z)|')
    plt.show()
