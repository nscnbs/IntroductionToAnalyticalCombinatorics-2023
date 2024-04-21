import numpy as np
import matplotlib.pyplot as plt

def direction_vectors(num_directions):
    angles = np.linspace(0, 2*np.pi, num_directions)
    vectors = [np.exp(1j * angle) for angle in angles]
    return vectors

def plot_direction_vectors(vectors):
    plt.figure(figsize=(8, 8))
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    for vector in vectors:
        plt.quiver(0, 0, vector.real, vector.imag, angles='xy', scale_units='xy', scale=1, color='r', alpha=0.5)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Kierunki zbliżania się do punktu z=0')
    plt.show()

num_directions = 24

vectors = direction_vectors(num_directions)
plot_direction_vectors(vectors)