def binary_search(arr, val, bot, top):  # бинарный поиск через цикл // значение, bot и top индексы
    while bot <= top:
        mid = bot + (top - bot) // 2  # середина массива
        if arr[mid] == val:  # выводим ответ, если равно
            return mid+1
        elif val > arr[mid]:  # меняем границы массива, если не равно
            bot = mid+1
        else:
            top = mid-1
    return -1  # при равенстве или изменении знака элемент отсутствует


if __name__ == '__main__':
    inp = input().split()
    sort_m = [int(inp[i]) for i in range(1, len(inp))]
    inp = input().split()
    search_m = [int(inp[i]) for i in range(1, len(inp))]

    answer = [str(binary_search(sort_m, dg, 0, len(sort_m)-1)) for dg in search_m]

    print(" ".join(answer))

