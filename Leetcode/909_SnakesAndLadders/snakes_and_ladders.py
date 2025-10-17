from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # PLEASE KILL THIS
        # идея в том чтобы сразу найти все возможные быстрее перемещения
        # и потом реализовать логику подсчета ходов
        size = len(board)
        last = size * size
        order = [] # показывает порядок перемещений
        shortcuts = {} # сами перемещения
        ordinal = 1 # нумерация клеток
        for row in reversed(board):
            if (ordinal // size) % 2 == 0:
                for col in row:
                    if col != -1:
                        order.append(ordinal)
                        shortcuts[ordinal] = col
                    ordinal += 1
            else:
                for col in reversed(row):
                    if col != -1:
                        order.append(ordinal)
                        shortcuts[ordinal] = col
                    ordinal += 1
        # если добавить set() посещенных вершин и логику к нему, то решения станет адекватным
        moves = deque([1])
        count_move = 0
        # а так проверяем можем ли дойти до финиша за 400 ходов
        while count_move <= 400:
            count_move += 1
            next_level = set()
            while moves:
                place = moves.popleft()
                # перемещение если есть шорткаты
                if order and place <= order[-1]:
                    not_blocked = []
                    for i in range(1, 7):
                        if place + i > last:
                            break
                        if place + i in shortcuts:
                            next_level.add(shortcuts[place + i])
                        else:
                            not_blocked.append(place + i)
                    if not_blocked:
                        next_level.add(not_blocked[-1])
                # обычное перемещение на 6 клеток
                else:
                    next_level.add(min(last, place + 6))
                # если в очереди появился последний элемент мы дошли
                if last in next_level:
                    return count_move
            moves = deque(next_level)
        return -1

    def snakesAndLaddersFixed(self, board: List[List[int]]) -> int:
        # 99% 85%
        size = len(board)
        last = size * size
        shortcuts = {}
        cell_num = 1
        for i in range(size - 1, -1, -1):
            if (size - i) % 2 == 1:
                for j in range(size):
                    if board[i][j] != -1:
                        shortcuts[cell_num] = board[i][j]
                    cell_num += 1
            else:
                for j in range(size - 1, -1, -1):
                    if board[i][j] != -1:
                        shortcuts[cell_num] = board[i][j]
                    cell_num += 1
        visited = {1}
        queue = deque([(1, 0)])
        while queue:
            position, moves = queue.popleft()
            if position == last:
                return moves
            for dice in range(1, 7):
                next_pos = position + dice
                if next_pos > last:
                    break
                final_pos = shortcuts.get(next_pos, next_pos)
                if final_pos not in visited:
                    visited.add(final_pos)
                    queue.append((final_pos, moves + 1))
        return -1


    def snakesAndLadders1(self, board: List[List[int]]) -> int:
        # 30% 99%
        n = len(board)
        target = n * n
        def get_position(square):
            """Convert square number to board coordinates"""
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:  # Even rows in 0-based indexing are right-to-left
                col = n - 1 - col
            return n - 1 - row, col  # Convert to board coordinates
        visited = set()
        queue = deque([(1, 0)])  # (position, moves)
        while queue:
            position, moves = queue.popleft()
            if position == target:
                return moves
            # Try all dice rolls from 1 to 6
            for dice in range(1, 7):
                next_pos = position + dice
                if next_pos > target:
                    break
                # Get board coordinates
                row, col = get_position(next_pos)
                # Check for snake or ladder
                if board[row][col] != -1:
                    next_pos = board[row][col]
                # If not visited, add to queue
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        return -1

    def snakesAndLadders2(self, board: List[List[int]]) -> int:
        # 91% 40%
        # board в одномерный массив
        oneDarray = []
        N = len(board)
        for i in range(len(board) - 1, -1, -1):
            if (N - i + 1) % 2 == 0:
                for j in range(N):
                    oneDarray.append(board[i][j])
            else:
                for k in range(N - 1, -1, -1):
                    oneDarray.append(board[i][k])

        queue = deque([[0, 0]])
        n = len(oneDarray) - 1
        while queue:
            curr, depth = queue.popleft()
            if curr >= n:
                return depth
            for i in range(1, 7):
                # помечаем клетки в которых были нулём и избегаем их
                if i + curr <= n and oneDarray[i + curr] != 0:
                    if oneDarray[i + curr] != -1:
                        queue.append([oneDarray[i + curr] - 1, depth + 1])
                    else:
                        queue.append([i + curr, depth + 1])
                    oneDarray[i + curr] = 0
        return -1



if __name__ == '__main__':
    Solution().snakesAndLaddersFixed([[-1,-1,-1],[-1,9,8],[-1,8,9]])
    Solution().snakesAndLaddersFixed([[-1,394,393,392,391,390,389,388,387,386,385,384,383,382,381,380,379,378,377,376],[356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375],[355,354,353,352,351,350,349,348,347,346,345,344,343,342,341,340,339,338,337,336],[316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335],[315,314,313,312,311,310,309,308,307,306,305,304,303,302,301,300,299,298,297,296],[276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295],[275,274,273,272,271,270,269,268,267,266,265,264,263,262,261,260,259,258,257,256],[236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255],[235,234,233,232,231,230,229,228,227,226,225,224,223,222,221,220,219,218,217,216],[196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215],[195,194,193,192,191,190,189,188,187,186,185,184,183,182,181,180,179,178,177,176],[156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175],[155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136],[116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135],[115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,98,97,96],[76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95],[75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56],[36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55],[35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16],[-1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]])
    Solution().snakesAndLadders2([[-1,-1],[-1,3]])
    Solution().snakesAndLadders2([[1,1,-1],[1,1,1],[-1,1,1]])
    Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])
    Solution().snakesAndLadders1([[-1,60,32,-1,-1,-1,59,-1],[34,1,15,9,13,25,63,26],[-1,-1,-1,-1,29,-1,-1,-1],[-1,-1,-1,27,-1,-1,-1,5],[6,59,-1,2,40,13,-1,-1],[-1,44,20,-1,-1,-1,58,-1],[-1,-1,9,-1,-1,23,-1,-1],[-1,-1,-1,46,27,6,-1,-1]])
    Solution().snakesAndLadders([[-1,-1,-1,63,-1,-1,-1,62,-1],[53,52,13,32,-1,-1,-1,-1,-1],[-1,-1,26,-1,73,-1,-1,-1,55],[-1,-1,-1,-1,74,-1,-1,-1,-1],[-1,-1,35,42,-1,45,-1,-1,-1],[81,-1,3,46,-1,-1,-1,-1,59],[74,-1,66,16,-1,-1,-1,-1,-1],[-1,-1,-1,28,-1,-1,81,-1,22],[-1,-1,-1,-1,61,17,39,21,-1]])
    Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
