from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # поиск колонки - target внутри или крайняя
        left_r, right_r = 0, len(matrix) - 1
        while left_r < right_r:
            mid = (left_r + right_r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            if matrix[mid][0] < target:
                left_r = mid + 1
            else:
                right_r = mid - 1
        else:
            target_row = left_r
        # ищем элемент в колонке
        left_c, right_c = 0, len(matrix[0]) - 1
        while left_c < right_c:
            mid = (left_c + right_c) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] < target:
                left_c = mid + 1
            else:
                right_c = mid - 1
        return target == matrix[target_row][left_c]

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        # работаем с индексами матрицы так, будто это одномерный массив
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # бест
        ans = False
        for row in matrix:
            idx = bisect_left(row,target)
            if idx < len(row) and row[idx] == target:
                ans = True
        return ans


if __name__ == '__main__':
    Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 100)
    Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)


