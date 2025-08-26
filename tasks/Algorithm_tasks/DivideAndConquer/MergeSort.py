from collections import deque  # для ускорения через popleft


def merge_sort(arr):  # обычная сортировка слиянием - находим середину, делим
    if len(arr) < 2:  # повторяем рекурсивно, пока не возникнут одиночки
        return 0, arr
    mid = len(arr) // 2
    c_l, arr_l = merge_sort(arr[:mid])
    c_r, arr_r = merge_sort(arr[mid:])
    c, merged = merge_count(deque(arr_l), deque(arr_r))  # потом соединяем все, сортируя и считая пары
    return c + c_r + c_l, merged


def merge_count(left, right):
    c = 0  # счетчик
    merged = []  # отсортированный массив
    while left and right:  # сделано через pop, можно было бы по индексам
        if left[0] > right[0]:
            c += len(left)  # если слева больше, то все элементы слева больше правого и образуют с ним пары
            merged.append(right.popleft())
        else:
            merged.append(left.popleft())
    merged.extend(left or right)  # если left или right кончился, второй присоединяем в конце и возвращаем счетчик и сортированный
    return c, merged


if __name__ == '__main__':
    n = int(input())
    inp = [int(x) for x in input().split()]

    count, _ = merge_sort(inp)  # таскал с собой переменную счетчик и вывел её в конце
    print(count)
