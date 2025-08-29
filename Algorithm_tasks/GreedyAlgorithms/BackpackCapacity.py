if __name__ == '__main__':
    count, capacity = [int(x) for x in input().split()]  # ничего такого
    things = sorted([[int(x) for x in input().split()] for i in range(count)], key=lambda thing: thing[0]/thing[1], reverse=True)   # сортировка по убыванию цены за килограмм
    price = 0
    for mon, cap in things:  # если влазит пихаем, если нет, пихаем, но не всё, конец...
        if cap <= capacity:
            capacity -= cap
            price += mon
        else:
            if capacity != 0:
                price += capacity * (mon / cap)
            break
    print('{:.3f}'.format(price))  # форматирование вывода
