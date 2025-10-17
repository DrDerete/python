class Solution:
    def totalNQueens(self, n: int) -> int:
        pos = []
        # идея - рекурентно расставить ферзей по свободным местам,
        # а места выбирать как незанятный столбец или л/п диагональ
        def backtrack(row):
            if row == n:
                pos.append(1)
            else:
                for col in range(n):
                    # Если клетка занята (т.е. в одной колонне или на диагоналях стоит ферзь), то пропускаем
                    if cols[col] == True or right_diagonals[row + col] or left_diagonals[row - col]:
                        continue
                    else:
                        # ферзь это правда
                        cols[col] = right_diagonals[row + col] = left_diagonals[row - col] = True
                        backtrack(row + 1)
                        cols[col] = right_diagonals[row + col] = left_diagonals[row - col] = False
        cols = [False] * n
        count_d = 2 * n - 1                     # диагонали шахматного поля
        left_diagonals = [False] * count_d      # \\\\
        right_diagonals = [False] * count_d     # ////
        backtrack(0)
        return sum(pos)

    def totalNQueens1(self, n: int) -> int:
        cnt = 0

        def dfs(row, col, diag, adiag):
            nonlocal cnt
            if row == n:
                cnt += 1
                return
            mask = ((1 << n) - 1) & ~(col | diag | adiag)
            while mask:
                p = mask & -mask
                mask -= p
                dfs(row + 1, col | p, (diag | p) << 1, (adiag | p) >> 1)

        dfs(0, 0, 0, 0)
        return cnt

if __name__ == '__main__':
    print(Solution().totalNQueens(2))
    print(Solution().totalNQueens(4))