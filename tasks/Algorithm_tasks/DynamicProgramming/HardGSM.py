def hard_gsm(arr, ln):
    accounting = [1]
    for i in range(1, ln):
        accounting.append(1)
        for j in range(0, i):
            if arr[j] >= arr[i] and accounting[i] < accounting[j]+1:
                accounting[i] += 1

    m = max(accounting)
    print(m)

    index_gsm = []
    for j in reversed(range(ln)):
        if accounting[j] == m:
            index_gsm.append(j+1)
            m -= 1
        if m == 0:
            break

    print(*list(reversed(index_gsm)))


if __name__ == '__main__':
    n = int(input())
    inp = [int(x) for x in input().split()]
    hard_gsm(inp, n)

