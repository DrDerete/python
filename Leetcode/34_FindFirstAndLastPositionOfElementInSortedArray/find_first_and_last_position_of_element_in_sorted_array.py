from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(find_first):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if find_first:
                        right = mid - 1  # Ищем первое вхождение
                    else:
                        left = mid + 1  # Ищем последнее вхождение
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        return [binary_search(True), binary_search(False)]