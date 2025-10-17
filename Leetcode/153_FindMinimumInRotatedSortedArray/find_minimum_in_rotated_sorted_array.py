from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # Минимум находится справа от mid
                left = mid + 1
            else:
                # Минимум находится слева (включая mid)
                right = mid
        return nums[left]