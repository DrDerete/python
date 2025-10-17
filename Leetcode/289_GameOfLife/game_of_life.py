from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changes = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                count_life = 0
                # строка выше
                if i > 0:
                    count_life += board[i - 1][j]
                    if j > 0:
                        count_life += board[i - 1][j - 1]
                    if j < len(board[0]) - 1:
                        count_life += board[i - 1][j + 1]
                # строка ниже
                if i < len(board) - 1:
                    count_life += board[i + 1][j]
                    if j > 0:
                        count_life += board[i + 1][j - 1]
                    if j < len(board[0]) - 1:
                        count_life += board[i + 1][j + 1]
                # клетки слева и справа
                if j > 0:
                    count_life += board[i][j - 1]
                if j < len(board[0]) - 1:
                    count_life += board[i][j + 1]
                # правила игры
                if board[i][j]:
                    if count_life < 2 or count_life > 3:
                        changes.append([i, j])
                else:
                    if count_life == 3:
                        changes.append([i, j])
        for change in changes:
            board[change[0]][change[1]] = 0 if board[change[0]][change[1]] else 1

if __name__ == '__main__':
    Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
