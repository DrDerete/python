from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        ans = []
        cycle = 0
        stop = len(matrix) * len(matrix[0])
        while True:
            ans.append(matrix[i][j])
            right_border = len(matrix[0]) - cycle - 1
            while j < right_border:
                j += 1
                ans.append(matrix[i][j])
            if len(ans) == stop:
                break
            bottom_border = len(matrix) - cycle - 1
            while i < bottom_border:
                i += 1
                ans.append(matrix[i][j])
            if len(ans) == stop:
                break
            left_border = cycle
            while j > left_border:
                j -= 1
                ans.append(matrix[i][j])
            if len(ans) == stop:
                break
            top_border = cycle + 1
            while i > top_border:
                i -= 1
                ans.append(matrix[i][j])
            cycle += 1
            j += 1
            if len(ans) == stop:
                break
        return ans

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        ans = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            # Top row
            result += matrix.pop(0)

            # Right column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Bottom row (reversed)
            if matrix:
                result += matrix.pop()[::-1]

            # Left column (bottom to top)
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    result.append(row.pop(0))

        return result

if __name__ == '__main__':
    print(Solution().spiralOrder1([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().spiralOrder1([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

