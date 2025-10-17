from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # Первая транзакция: слева направо
        left = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_price)

        # Вторая транзакция: справа налево
        right = [0] * n
        max_price = prices[-1]

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i + 1], max_price - prices[i])

        # Комбинируем обе транзакции
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left[i] + right[i])

        return max_profit