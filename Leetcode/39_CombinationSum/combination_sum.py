from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # абсолютно аналогично прошлым
        result = []

        path = []
        def backtrack(start, current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, current_sum + candidates[i])
                path.pop()

        backtrack(0, 0)
        return result

    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        # А ЭТО ЛЮТЫЙ НЕОЧЕВИДНЫЙ УМ
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        # располагаем значения по массиву таким образом, что сумма элементов является индексом
        # исходя из этой идеи идем по кандидатам и заполняем ячейки массива
        for candidate in candidates:
            for amount in range(candidate, target + 1):
                for combination in dp[amount - candidate]:
                    dp[amount].append(combination + [candidate])
        # [[[]], [], [], [], [], [], [], []] после первой итерации цикла -> [[[]], [], [[2]], [], [[2, 2]], [], [[2, 2, 2]], []]
        # в последней ячейке образуется ответ
        return dp[target]

if __name__ == '__main__':
    Solution().combinationSum1([2, 3, 6, 7], 7)
