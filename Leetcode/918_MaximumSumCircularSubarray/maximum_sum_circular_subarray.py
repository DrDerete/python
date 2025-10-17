from typing import List


class Solution:
    # следующая идея - есть максимальная и минимальная подпоследовательности,
    # они не могут одновременно быть внутри nums, поэтому помогут одолеть его цикличность
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_kadane = min_kadane = nums[0]
        cur_max = cur_min = total_sum = 0
        for num in nums:
            # считаем максимум
            cur_max = max(num, cur_max + num)
            max_kadane = max(max_kadane, cur_max)
            # считаем минимум
            cur_min = min(num, cur_min + num)
            min_kadane = min(min_kadane, cur_min)
            # сумма для случая когда максимум находится в цикле
            total_sum += num
        # обрабатываем исключение
        if max_kadane < 0:
            return max_kadane
        # максимум для случаев: максимум внутри или максимум вЦИКЛ
        return max(max_kadane, total_sum - min_kadane)


if __name__ == '__main__':
    Solution().maxSubarraySumCircular([5,4,-1,7,8])
    Solution().maxSubarraySumCircular([3,-1,2,-1])
    Solution().maxSubarraySumCircular([5,-3,5])
    Solution().maxSubarraySumCircular([1,-2,3,-2])
    Solution().maxSubarraySumCircular([-3,-2,-3])
    Solution().maxSubarraySumCircular([1, -2, 3, -2, 1])
