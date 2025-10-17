from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(word_idx, row, col):
            # проверяем что ячейка не посещена и не отличается от нужной буквы
            if board[row][col] == "" or board[row][col] != word[word_idx]:
                return False
            # если последняя буква слова
            if word_idx + 1 == len(word):
                return True
            # проход по полю во всех направлениях с рекурсией
            ch = board[row][col]
            board[row][col] = ""
            for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
               if  0 <= row + i < len(board) and 0 <= col + j < len(board[0]):
                   if backtrack(word_idx + 1, row + i, col + j):
                       return True
            board[row][col] = ch
            return False

        for i_idx in range(len(board)):
            for j_idx in range(len(board[0])):
                if backtrack(0, i_idx, j_idx):
                    return True
        return False

    # ускоряем, заранее подсчитывая буквы
    def exist1(self, board: List[List[str]], word: str) -> bool:
        board_chars = Counter(ch for row in board for ch in row)
        word_chars = Counter(word)
        # если каких-то букв не хватает
        if any(word_chars[ch] > board_chars[ch] for ch in word_chars):
            return False
        # начинаем поиск с самой редкой буквы
        if word_chars[word[0]] > word_chars[word[-1]]:
            word = word[::-1]

        def backtrack(word_idx, row, col):
            if word_idx == len(word):
                return True

            if (row < 0 or row >= len(board) or
                    col < 0 or col >= len(board[0]) or
                    board[row][col] != word[word_idx]):
                return False

            board[row][col] = "#"

            found = (backtrack(word_idx + 1, row + 1, col) or
                     backtrack(word_idx + 1, row - 1, col) or
                     backtrack(word_idx + 1, row, col + 1) or
                     backtrack(word_idx + 1, row, col - 1))

            board[row][col] = word[word_idx]
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(0, i, j):
                    return True
        return False

if __name__ == '__main__':
    Solution().exist([["a"]], "a")
    Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
