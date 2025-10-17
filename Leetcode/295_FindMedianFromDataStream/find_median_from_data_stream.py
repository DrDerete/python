import heapq


class MedianFinder:

    def __init__(self):
        self.minVals = []  # max-heap для левой половины (меньшие числа)
        self.maxVals = []  # min-heap для правой половины (большие числа)

    def addNum(self, num: int) -> None:
        # Всегда добавляем в minVals (max-heap) сначала
        heapq.heappush(self.minVals, -num)

        # Балансировка 1: убеждаемся, что максимальный элемент в minVals <= минимальный элемент в maxVals
        if self.minVals and self.maxVals and -self.minVals[0] > self.maxVals[0]:
            minVal = -heapq.heappop(self.minVals)
            heapq.heappush(self.maxVals, minVal)

        # Балансировка 2: поддерживаем правильное соотношение размеров
        # minVals может быть максимум на 1 элемент больше maxVals
        if len(self.minVals) > len(self.maxVals) + 1:
            heapq.heappush(self.maxVals, -heapq.heappop(self.minVals))
        elif len(self.maxVals) > len(self.minVals):
            heapq.heappush(self.minVals, -heapq.heappop(self.maxVals))

    def findMedian(self) -> float:
        if len(self.minVals) == len(self.maxVals):
            return (-self.minVals[0] + self.maxVals[0]) / 2
        elif len(self.minVals) > len(self.maxVals):
            return -self.minVals[0]
        else:
            return self.maxVals[0]