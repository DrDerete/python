def find_gsm(arr, ln):  # наибольшая длинна подпоследовательности элементов в массиве; j>i -> arr[j] % arr[i] == 0
    accounting = [1 for i in range(ln)]  # массив учета
    for i in range(ln):  # \можно было бы по другому построить массив учета, постепенно добавляя в него элементы и каждый раз полностью проходя основной до длинны массива учета
        for j in range(i+1, ln):  # \сделал в HardGSM.py
            if arr[j] % arr[i] == 0 and accounting[i] == accounting[j]:  # если элемент кратен и в массиве учета, получается лучший результат, то:
                accounting[j] += 1  # обновляем массив учета
    return max(accounting)  # максимальный элемент это ответ


if __name__ == '__main__':
    n = int(input())
    inp = [int(x) for x in input().split()]
    print(find_gsm(inp, n))
