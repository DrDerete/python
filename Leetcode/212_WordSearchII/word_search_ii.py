from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 32 % 82%(было) ->(удаление пустых вершин) -> 78% 88-95%(сейчас)
        # идея - используем трай для сравнений и быстрого выхода из рекурентной функции
        trie = {}
        for w in words:
            head = trie
            for ch in w:
                if ch not in head:
                    head[ch] = {}
                head = head[ch]
            head["#"] = w

        ans = []
        def dfs(i, j, ch_in_trie, vis):
            # записываем ответ, если дошли до слова с "#"
            if "#" in ch_in_trie:
                ans.append(ch_in_trie.pop("#"))
            # избегаем граничных условий, посещенных вершин и слов не из трая
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] not in ch_in_trie:
                return
            if (i, j) in vis:
                return
            else:
                vis.add((i, j))
            # рекурентно идем по полю
            dfs(i + 1, j, ch_in_trie[board[i][j]], vis)
            dfs(i - 1, j, ch_in_trie[board[i][j]], vis)
            dfs(i, j + 1, ch_in_trie[board[i][j]], vis)
            dfs(i, j - 1, ch_in_trie[board[i][j]], vis)
            # убираем за собой, чтобы буква могла использоваться в другом слове
            vis.remove((i, j))
            # если вершина лист - удаляем её
            if not ch_in_trie[board[i][j]]:
                del ch_in_trie[board[i][j]]

        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie, visited)
        return ans

    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 92% 95% - обходимся только траем, меняя само поле board
        # и проверка до рекурсии. ИЗ 600ms в 400ms ощутимо
        WORD_KEY = '#'

        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[WORD_KEY] = word

        result = []
        rows, cols = len(board), len(board[0])

        def backtrack(row, col, parent):
            char = board[row][col]
            curr_node = parent[char]

            word_match = curr_node.pop(WORD_KEY, False)
            if word_match:
                result.append(word_match)

            board[row][col] = '#'

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset
                if (0 <= new_row < rows and 0 <= new_col < cols and
                        board[new_row][new_col] in curr_node):
                    backtrack(new_row, new_col, curr_node)

            board[row][col] = char

            if not curr_node:
                parent.pop(char)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    backtrack(row, col, trie)

        return result


if __name__ == '__main__':
    Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain","hklf", "hf"])
    Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])

