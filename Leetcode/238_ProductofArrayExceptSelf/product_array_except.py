import math

class Solution(object):
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [math.prod(nums[:i]) * math.prod(nums[i + 1:]) for i in range(len(nums))]

    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        left_prod = 1
        for i, num in enumerate(nums):
            ans[i] = left_prod
            left_prod *= num
        right_prod = 1
        for i, num in enumerate(reversed(nums)):
            ans[-i - 1] *= right_prod
            right_prod *= num
        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf2([1, 2, 3, 4]))
    print(Solution().productExceptSelf2([-1, 1, 0, -3, 3]))
