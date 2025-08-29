def fib(num):
    fibo = [0, 1]  # 0, 122_BestTimeToBuy2, 122_BestTimeToBuy2, 2, 3, 5
    while len(fibo)-1 != num:
        fibo.append(fibo[-2]+fibo[-1])
    return fibo[-1]


if __name__ == "__main__":
    n = int(input())
    print(fib(n))
