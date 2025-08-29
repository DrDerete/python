def fib_digit(n):
    fib = [0, 1]
    while len(fib)-1 != n:
        fib.append((fib[-1]+fib[-2]) % 10)
    return fib[-1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
