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


scaling_factor = 0.5

n_values = range(1, 1025)

a_values = [a(n) * scaling_factor for n in n_values]

"""
def wyniki():
    print("s(n)")
    for m in n_values:
        print(m, s(m))
    print("\n\ns(n)*scaling_factor")
    k=0
    for i in s_values:
        k=k+1
        print(k, i)


wyniki()
"""
#max_s_value = max(s_values)
#normalized_s_values = [value / max_s_value for value in s_values]


#plt.plot(n_values, normalized_s_values, label='Normalized s(n)')
plt.plot(n_values, a_values, label='s(n) * scaling_factor')
plt.xlabel('n')
plt.ylabel('s(n)')
plt.legend()
plt.show()
