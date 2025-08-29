if __name__ == '__main__':
    digit = int(input())
    optim = set()
    for i in range(1, digit+1):  # жадный алгоритм
        optim.add(i)  # сразу жадно добавляем число
        if digit-i in optim:  # если число не подходит, удаляем и жадно переходим к другому
            optim.remove(i)
            continue
        digit -= i
        if digit == 0:  # обрабатываем конец, естественно жадно
            break
    print(len(optim))  # жадно получаем оптимальный вариант
    print(*optim)
