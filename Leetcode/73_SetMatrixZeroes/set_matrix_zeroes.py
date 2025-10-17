from typing import  List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        for row in zero_row:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in zero_col:
            for row in range(len(matrix)):
                matrix[row][col] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        # в качестве память выступают первые столбец и строка матрицы,
        # поэтому необходимо запомнить были ли в них нули изначально
        # и в конце их занулить
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark zeros on first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeroes based on marks
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

if __name__ == '__main__':
    Solution().setZeroes([[1,1,1], [1,0,1], [1,1,1]])
    Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
