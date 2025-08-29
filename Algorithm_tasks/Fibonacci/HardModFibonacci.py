def pisano_period(p):  # подсчет периода от числа p для последовательности чисел фибоначи
    per, cur = 0, 1
    t = 0
    while True:
        t += 1
        per, cur = cur, (per+cur) % p
        if per == 0 and cur == 1:  # просто алгоритм фибоначи, пока не вернешься в начало
            return t


def fib_mod(n, m):
    fib = [0, 1]
    period = pisano_period(m)  # период найден
    n = n % period - 1  # переход к нужному элементу
    if n == -1:
        return 0
    elif n == 0:
        return 1
    else:
        while n != 0:
            n -= 1
            fib.append((fib[-1]+fib[-2]) % m)
            fib.pop(0)
        return fib[-1]  # подсчет и вывод с учетом 2 исключений


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
