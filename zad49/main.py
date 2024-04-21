import matplotlib.pyplot as plt
import numpy as np

#Oblicza wartości p(n) na podstawie równania rekurencyjnego
def pn(n):
    pns = [1.0]

    for j in range(1, n + 1):
        pns.append(sum(sigma(j) * pj for pj in pns[:j]) / j)

    return pns[n - 1] / n

# Oblicza sumę dzielników liczby n
def sigma(n):
    return sum(x for x in range(1, n + 1) if n % x == 0)

def main():
    n_values = list(range(1, 101))
    s_values = [pn(n) for n in n_values]

    for i, value in enumerate(s_values, start=1):
        print(f"{i} = {value}")

    # Plotting s(n)
    plt.plot(n_values, s_values, label='p(n)/n')
    plt.title("Zależność p(n)/n od n")
    plt.xlabel('n')
    plt.ylabel('p(n)/n')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
