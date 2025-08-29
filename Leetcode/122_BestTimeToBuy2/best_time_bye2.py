class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bye = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                ans += prices[i - 1] - bye
                bye = prices[i]
        return ans

    def maxProfit2(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit2([2, 4, 1]))
    print(Solution().maxProfit2([7, 2, 5, 3, 6, 1]))
