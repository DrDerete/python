class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_i = None
        min_i = None
        candidate = None
        for i in range(len(prices)):
            if candidate is None:
                if max_i is None:
                    max_i, min_i = i, i
                elif prices[i] > prices[max_i]:
                    max_i = i
                elif prices[i] < prices[min_i]:
                    candidate = i
            else:
                if prices[i] < prices[candidate]:
                    candidate = i
                if prices[i] > prices[candidate] + prices[max_i] - prices[min_i]:
                    min_i = candidate
                    max_i = i
                    candidate = None
        return prices[max_i] - prices[min_i]

    def maxProfit2(self, prices):
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy
        return profit

if __name__ == '__main__':
    print(Solution().maxProfit2([2, 4, 1]))
    print(Solution().maxProfit2([7, 2, 5, 3, 6, 1]))
