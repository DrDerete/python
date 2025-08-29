class Combinator(object):

    def __init__(self, n, k):
        self.MASSIF = [x for x in range(n)]  # сам массив элементов
        self.END_ELEMENTS = [self.MASSIF[i] for i in range(len(self.MASSIF)-k, len(self.MASSIF))]  # наша остановочка

    def print_combination(self, step=None, element=0, combination=None):  # с помощью рекурсии
        if combination is None:
            combination = []
        if step is None:
            step = len(self.END_ELEMENTS)
        while True:
            if step != 0:
                combination.append(self.MASSIF[element])
                step -= 1
                self.print_combination(step, element+1, combination)  # вот сама рекурсия
                if len(combination) == 0:
                    return  # Это полноправный конец
                elif combination[-1] == self.END_ELEMENTS[len(combination)-1]:
                    combination.pop()
                    return  # Когда все сочетания выведены, возвращаемся на шаг раньше из рекурсии
                else:
                    combination[-1] += 1  # Когда вернулись из рекурсии, подравниваем параметры и дальше снова вглубь и печатаем
                    element += 1
                    step += 1
            else:  # доходим до конца и печатаем все сочетания
                for i in range(combination[-1], len(self.MASSIF)):
                    combination.pop()
                    combination.append(self.MASSIF[i])
                    print(*combination)
                combination.pop()
                return


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    if inp[1] == 1 or inp[0] > inp[1] or inp[0] < 1:
        print(0)
    else:
        Combinator(inp[1], inp[0]).print_combination()  # тут реализована именно печать, чтобы выводить элементы, надо создавать объект генератор, с помощью которого уже осуществлять вывод
