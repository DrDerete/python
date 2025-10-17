from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # Начинаем с предпоследней строки и идем вверх
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Минимум из двух возможных путей + текущее значение
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]