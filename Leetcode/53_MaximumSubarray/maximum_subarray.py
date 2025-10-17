from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        num_sum = nums[0]
        for n in nums[1:]:
            num_sum = max(num_sum + n, n)
            ans = max(ans, num_sum)
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        # это топ на литкоде
        s = 0
        maxsum = float('-inf')
        for num in nums:
            s += num
            if s > maxsum:
                maxsum = s
            if s < 0:
                s = 0
        return maxsum

if __name__ == '__main__':
    Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
