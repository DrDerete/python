from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1 or k == 0:
            return 0

        # Если k достаточно большое, задача сводится к неограниченным транзакциям
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[i][j] - максимальная прибыль после j транзакций к дню i
        dp = [[0] * (k + 1) for _ in range(n)]

        for j in range(1, k + 1):
            min_cost = prices[0]
            for i in range(1, n):
                # min_cost = минимальная цена с учетом предыдущей прибыли
                min_cost = min(min_cost, prices[i] - dp[i - 1][j - 1])
                # Максимальная прибыль = максимум между:
                # - не продавать сегодня (взять предыдущую прибыль)
                # - продать сегодня (цена - min_cost)
                dp[i][j] = max(dp[i - 1][j], prices[i] - min_cost)

        return dp[n - 1][k]