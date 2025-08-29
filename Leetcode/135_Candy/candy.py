class Solution(object):
    def candy1(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 99-90% - скорость 95% - память (хотел не использовать массив)
        rewards, cand = 1, 1  # общее количество награды в конфетах и переменная конфет
        last_drop = None  # нужна для того, чтобы знать какое было значение у cand в момент когда сбросили награду
        low_streak = 0  # поскольку награда была сброшена, а дальше понадобится (а может и нет) награда меньше, необходимо считать сколько конфет надо додать
        # причем last_drop показывает, надо ли будет давать конфеты тому, на ком была сброшена награда
        # пример: ratings = [1 6 3 1] получают [1 3 2 1], если увечить серию [1 6 5 4 3 2 1], то и второй(i = 1) получает больше
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                low_streak = 0
                last_drop = None
                if ratings[i] > ratings[i - 1]:  # в случае увеличения оценки, награда обязана увеличиться
                    cand += 1
                    rewards += cand
                else:  # равенство дает свободу, но в силу собственной выгоды занижаем награду в минимум
                    cand = 1
                    rewards += cand
            else:  # в случае ухудшения награда, должна уменьшится, но не ниже 1
                low_streak += 1  # добавка конфет
                if cand == 1:
                    if last_drop is None:  # если сброса награды не было и мы начинали с 1
                        rewards += low_streak + 1
                    else:  # если награда сбрасывалась
                        if low_streak == last_drop:  # проверяем не обделили ли участника с оценкой лучше, чем у серии лузеров
                            low_streak += 1
                        rewards += low_streak  # выдаем конфеты
                else:  # вот тут сбрасываем награду в минимум и запоминаем на ком, потому что ему может потребоваться добавка
                    rewards += 1
                    last_drop = cand
                    cand = 1
        return rewards

    def candy2(self, ratings):
        # 79 75%
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)


if __name__ == '__main__':
    print(Solution().candy1([1, 2, 3, 1, 0]))
    print(Solution().candy1([1, 2, 0, 3, 2, 1]))
    print(Solution().candy1([1, 3, 2, 2, 1]))
    print(Solution().candy1([1, 0, 2]))
    print(Solution().candy1([1, 2, 2]))
