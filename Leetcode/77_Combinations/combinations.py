from typing import List, Any, Generator


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # рекурсия - проход по числам с рекурсивным вызовом на следующий разряд
        ans = []
        def backtracking(start, comb):
            if len(comb) == k:
                ans.append(comb.copy())
                return
            for num in range(start, n + 1):
                comb.append(num)
                backtracking(num + 1, comb)
                comb.pop()
        backtracking(1, [])
        return ans

    def combine1(self, n: int, k: int) -> List[List[int]]:
        # comb снаружи
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)
        return res

    def combine2(self, n: int, k: int) -> Generator[list[int], Any, None]:
        # ЖЁСТКО - генератор через индексы, как itertools
        indices = list(range(1, k + 1))
        yield indices[:]

        while True:
            i = k - 1
            while i >= 0 and indices[i] == n - k + i + 1:
                i -= 1

            if i < 0:
                break
            indices[i] += 1
            for j in range(i + 1, k):
                indices[j] = indices[j - 1] + 1

            yield indices[:]
    
if __name__ == '__main__':
    Solution().combine(4, 2)


