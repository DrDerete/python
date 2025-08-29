class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        beg, s = 0, 0
        ans = None
        for i in range(len(nums)):
            s += nums[i]
            if s >= target:
                while s - nums[beg] >= target:
                    s -= nums[beg]
                    beg += 1
                if ans is None:
                    ans = i - beg + 1
                elif ans > i - beg + 1:
                    ans = i - beg + 1
        return 0 if ans is None else ans

    def minSubArrayLen1(self, target, nums):
        left, s = 0, 0
        ans = float("inf")
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        if ans == float("inf"):
            return 0
        return ans




if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(Solution().minSubArrayLen(4, [1, 4, 4]))
    print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
