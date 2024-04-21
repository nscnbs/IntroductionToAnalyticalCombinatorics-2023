import matplotlib.pyplot as plt


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


def wyniki(n_max):
    for i in range(1, n_max+1):
        print(i, sd(i))


def plot_s(n_max):
    x_values = list(range(1, n_max + 1))
    y_values = [s(i) for i in x_values]
    plt.plot(x_values, y_values)
    plt.xlabel('n')
    plt.ylabel('s(n)')
    plt.title(f'Wykres funkcji s(n) dla n ∈ {{1,..., {n_max}}}')
    plt.show()


if __name__ == "__main__":
    wyniki(1024)
    plot_s(1024)

    #wyniki(4096)
    #plot_s(4096)
