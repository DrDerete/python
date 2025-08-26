class Permutator(object):  # получение элемента размещения с помощью Генератора \\ сделано как в itertools

    def __init__(self, n, k):
        self.MAS = [x for x in range(n)]  # надо сохранять индексы вводного итератора, но тут работа с числами, поэтому без них
        if k > len(self.MAS):
            print("Предметов больше, чем коробок!!!")
            return  # исключение
        self.END = list(range(n, n-k, -1))  # по этому массиву происходит реализация цикла
        self.__start_print()

    def __start_print(self):
        for perm in self.__get_perm():  # запускаем генератор и принтим то, что он возвращает
            print(*perm)

    def __get_perm(self):
        yield tuple(self.MAS[i] for i in range(len(self.END)))
        while True:
            for i in reversed(range(len(self.END))):  # сам цикл
                self.END[i] -= 1
                if self.END[i] == 0:
                    self.MAS[i:] = self.MAS[i+1:] + self.MAS[i:i+1]  # когда все комбинации для первого i опробованы, приводим все к изначальному виду и идем вглубь, а там всё по новой
                    self.END[i] = len(self.MAS) - i
                else:
                    j = self.END[i]
                    self.MAS[i], self.MAS[-j] = self.MAS[-j], self.MAS[i]  # меняем местами элементы в изначальном массиве и выводим
                    yield tuple(self.MAS[i] for i in range(len(self.END)))
                    break
            else:
                return


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    Permutator(inp[0], inp[1])
