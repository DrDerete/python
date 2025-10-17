from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # проходим по каждому с каждым, который не был использован, рекурсия аналогично combination
        ans = []
        n = len(nums)
        permute = []
        def permute_index(vis):
            if len(permute) == n:
                ans.append(permute[:])
                return
            for i in range(n):
                if i not in vis:
                    permute.append(nums[i])
                    vis.add(i)
                    permute_index(vis)
                    permute.pop()
                    vis.remove(i)
        visited = set()
        permute_index(visited)
        return ans

    def permute1(self, nums):
        # добавляем каждую цифру к остальным перестановкам, получая новые виды перестановок,
        # [] -> [1] -> [1, 2] [2, 1] -> [3, 1, 2] [1, 3, 2], [1, 2, 3] и ...  |  ваууу
        if not nums:
            return [[]]
        result = [[]]
        for num in nums:
            new_result = []
            for perm in result:
                for i in range(len(perm) + 1):
                    new_result.append(perm[:i] + [num] + perm[i:])
            result = new_result
        return result

if __name__ == '__main__':
    Solution().permute1([1, 2, 3])

