from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    Solution().searchInsert([1,3,5,6], 7)
    Solution().searchInsert([1,3,5,6], 2)
    Solution().searchInsert([1,3,5,6], 5)