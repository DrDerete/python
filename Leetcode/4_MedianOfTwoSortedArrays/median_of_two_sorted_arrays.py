from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Гарантируем, что nums1 - меньший массив
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Разбиваем общий массив на две равные части
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Находим граничные элементы
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Проверяем корректность разбиения
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Нашли правильное разбиение
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Слишком много элементов из nums1 в левой части
                right = partition1 - 1
            else:
                # Слишком мало элементов из nums1 в левой части
                left = partition1 + 1
        return
