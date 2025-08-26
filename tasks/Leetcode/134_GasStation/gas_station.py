class Solution(object):
    # найти элемент с которого накопительная разность массивов не отрицательна
    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas_bank = 0
        all_gas = 0
        ans = -1
        for i in range(len(gas)):
            d_gas = gas[i] - cost[i]
            if gas_bank + d_gas >= 0:
                gas_bank += d_gas
                if ans == -1:
                    ans = i
            else:
                gas_bank = 0
                ans = -1
            all_gas += d_gas
        if all_gas < 0:
            ans = -1
        return ans

    def canCompleteCircuit2(self, gas, cost):
        # выйгрыш в скорости 90-60% 63%
        if sum(gas) < sum(cost):
            return -1
        bank, ans = 0, 0
        for i in range(len(gas)):
            bank += gas[i] - cost[i]
            if bank < 0:
                bank = 0
                ans = i + 1
        return ans

    def canCompleteCircuit3(self, gas, cost):
        # выигрыш в памяти 47% 97%
        n = len(gas)
        i = j = n - 1
        cnt = s = 0
        while cnt < n:
            s += gas[j] - cost[j]
            cnt += 1
            j = (j + 1) % n
            while s < 0 and cnt < n:
                i -= 1
                s += gas[i] - cost[i]
                cnt += 1
        return -1 if s < 0 else i


if __name__ == '__main__':
    print(Solution().canCompleteCircuit2([1, 2, 3, 4, 5, 1, 9], [3, 4, 5, 1, 2, 9, 1]))
    print(Solution().canCompleteCircuit2([2, 3, 4], [3, 4, 3]))
    print(Solution().canCompleteCircuit2([3, 1, 1], [1, 2, 2]))
    print(Solution().canCompleteCircuit2([3, 1, 2, 5, 4], [4, 1, 1, 2, 3]))
