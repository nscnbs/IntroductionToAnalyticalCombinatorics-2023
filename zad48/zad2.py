import matplotlib.pyplot as plt
import math


def sd(n):
    suma = 0
    while n > 0:
        suma += n % 2
        n //= 2
    return suma

def s(n):
    suma = 0
    while n > 0:
        suma += sd(n)
        n -= 1
    return suma


def a(n):
    if n <= 0:
        return 0
    else:
        return math.log2(n)*n


def wyniki(n_max):
    print("a(n)")
    for i in range(1, n_max+1):
        print(i, a(i))
    print("s(n)")
    for i in range(1, n_max+1):
        print(i, s(i))
    print("s(n) - a (n)")
    for i in range(1, n_max+1):
        print(i, s(i)-a(i))

scaling_factor = 0.5


def plot_difference(n_max):
    x_values = list(range(1, n_max + 1))
    y_values_s = [s(i) for i in x_values]
    y_values_asymptotyka = [a(i) * scaling_factor for i in x_values]

    difference_values = [s_n - a_n for s_n, a_n in zip(y_values_s, y_values_asymptotyka)]

    plt.plot(x_values, difference_values) #y_values_asymptotyka)
    plt.xlabel('n')
    plt.ylabel('s(n) - asymptotyka(n)')
    plt.title(f'Wykres funkcji s(n) - asymptotyka(n) dla n ∈ {{1,..., {n_max}}}')
    plt.show()


if __name__ == "__main__":
    wyniki(1024)
    plot_difference(1024)
