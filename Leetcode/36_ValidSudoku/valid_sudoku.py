from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # проверка колонок
        for row in board:
            checker = {}
            for val in row:
                if val != ".":
                    if val in checker:
                        return False
                    checker[val] = None
        # проверка строк
        for i in range(9):
            checker = {}
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in checker:
                        return False
                    checker[board[j][i]] = None
        # проверка квадратов
        squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sq = []
                if board[i][j] != ".":
                    sq.append(board[i][j])
                if board[i][j + 1] != ".":
                    sq.append(board[i][j + 1])
                if board[i][j + 2] != ".":
                    sq.append(board[i][j + 2])
                if board[i + 1][j] != ".":
                    sq.append(board[i + 1][j])
                if board[i + 1][j + 1] != ".":
                    sq.append(board[i + 1][j + 1])
                if board[i + 1][j + 2] != ".":
                    sq.append(board[i + 1][j + 2])
                if board[i + 2][j] != ".":
                    sq.append(board[i + 2][j])
                if board[i + 2][j + 1] != ".":
                    sq.append(board[i + 2][j + 1])
                if board[i + 2][j + 2] != ".":
                    sq.append(board[i + 2][j + 2])
                squares.append(sq)
        for square in squares:
            checker = {}
            for dig in square:
                if dig in checker:
                    return False
                checker[dig] = None

        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        for row in board:
            checker = set()
            for val in row:
                if val != ".":
                    if val in checker:
                        return False
                    checker.add(val)
        for i in range(9):
            checker = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in checker:
                        return False
                    checker.add(board[j][i])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                checker = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] != ".":
                            if board[row][col] in checker:
                                return False
                            checker.add(board[row][col])
        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku2(
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    ))
    print(Solution().isValidSudoku2(
        [
            [".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]]
    ))

