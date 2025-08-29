from bisect import bisect_left, bisect_right


def quick_sort(arr):  # быстро сортируем
    if len(arr) <= 1:
        return arr
    else:
        stem = arr[len(arr) // 2]
        left = [x for x in arr if x < stem]
        mid = [x for x in arr if x == stem]
        right = [x for x in arr if x > stem]
        return quick_sort(left)+mid+quick_sort(right)


def check_inclusion():
    beg_s = quick_sort(begins)
    end_s = quick_sort(ends)
    answer = []
    for p in points:
        b_l = bisect_right(beg_s, p)  # находит индекс, такой, что все элементы beg_s <= p, будут слева, то есть прямая началась до точки
        e_l = bisect_left(end_s, p)  # то же самое, но beg_s < p; прямая закончилась строго до точки
        answer.append(b_l - e_l)  # разность даёт количество прямых, которым принадлежит точка
    print(*answer)


if __name__ == '__main__':
    c_l, c_p = [int(x) for x in input().split()]
    lines = [[int(x) for x in input().split()] for i in range(c_l)]
    points = [int(x) for x in input().split()]

    begins = [lines[i][0] for i in range(c_l)]
    ends = [lines[i][1] for i in range(c_l)]

    check_inclusion()



