from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # tails[i] хранит наименьший возможный последний элемент
        # возрастающей подпоследовательности длины i+1
        tails = []

        for num in nums:
            # Бинарный поиск позиции для вставки
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # Если num больше всех элементов в tails, добавляем в конец
            if left == len(tails):
                tails.append(num)
            else:
                # Заменяем элемент в позиции left на num
                tails[left] = num

        return len(tails)