def inverse_series(f, n):
    a = [f(i) for i in range(n)]
    results = [0.0] * n
    results[0] = 1.0 / f(0)

    for i in range(1, n):
        results[i] = -1.0 / a[0] * sum(a[i - k] * results[k] for k in range(i))

    return results

def f1(n):
    return 1.0

def f2(n):
    return 2.0**n

def f3(n):
    if n == 1 or n == 0:
        return 1.0
    else:
        return f3(n - 1) * float(n)

def f4(n):
    return 1.0 / f3(n)

def main():
    n = 10
    
    print("1. f(n) = 1:")
    for i, result in enumerate(inverse_series(f1, n), start=0):
        print(f"b{i}: {result}")

    print("\n2. f(n) = 2n:")
    for i, result in enumerate(inverse_series(f2, n), start=0):
        print(f"b{i}: {result}")

    print("\n3. f(n) = n!:")
    for i, result in enumerate(inverse_series(f3, n), start=0):
        print(f"b{i}: {result}")

    print("\n4. f(n) = 1/n!:")
    for i, result in enumerate(inverse_series(f4, n), start=0):
        print(f"b{i}: {result}")

if __name__ == "__main__":
    main()
