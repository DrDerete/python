from typing import List

class Solution:
    def __init__(self):
        self.region = None

    # не оптимально
    def solve(self, board: List[List[str]]) -> None:
        self.region = []
        # функция закрашивания
        def dfs(row, col):
            if board[row][col] == "O":
                if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                    return True
                board[row][col] = "X"
                self.region.append([row, col])
                p1 = dfs(row + 1, col)
                p2 = dfs(row - 1, col)
                p3 = dfs(row, col + 1)
                p4 = dfs(row, col - 1)
                return p1 or p2 or p3 or p4
            else:
                return False
        # проходимся по массиву и закрашиваем всё
        undo = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if dfs(i, j):
                        if self.region:
                            undo.append(self.region.copy())
                    self.region.clear()
        # возвращаем зону, которую закрасили в процессе
        while undo:
            zone = undo.pop()
            for cell in zone:
                board[cell[0]][cell[1]] = "O"


class Solution1:
    # можно пройти по краю и сразу отметить неизменяемые клетки
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        # раскраска клеток в E
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'E'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        # проходим по границам
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        # O -> X и E -> O ___готовО
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

if __name__ == '__main__':
    inp = [["O","O","O"],["O","O","O"],["O","O","O"]]
    inp1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(inp)

