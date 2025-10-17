from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    # 12% 68%
    def construct(self, grid: List[List[int]]) -> 'Node':
        # идём вглубь, пока не дойдем до создания node
        def build(r1, c1, size):
            if size == 1:
                return Node(grid[r1][c1] == 1, True, None, None, None, None)
            # ориентируемся пл центру сетки
            half = size // 2
            tl = build(r1, c1, half)
            tr = build(r1, c1 + half, half)
            bl = build(r1 + half, c1, half)
            br = build(r1 + half, c1 + half, half)
            # если образованные листья одинаковы - соединяем их
            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
                    tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)
            # в противном случае возвращаемся вершину с указанными листьями
            return Node(False, False, tl, tr, bl, br)

        return build(0, 0, len(grid))

    # в этом решение сначала проверяем сетку, а потом создаём
    # 81% 68%
    def construct1(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def is_uniform(r, c, size):
            val = grid[r][c]
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def build(r, c, size):
            uniform, val = is_uniform(r, c, size)
            if uniform:
                return Node(bool(val), True, None, None, None, None)

            half = size // 2
            return Node(False, False,
                        build(r, c, half),
                        build(r, c + half, half),
                        build(r + half, c, half),
                        build(r + half, c + half, half))

        return build(0, 0, n)

    # 97% 13%
    # самое быстрое на основе префиксной суммы
    def construct2(self, grid: List[List[int]]) -> 'Node':
        def build(r1, c1, size):
            # смотрим на значение префиксов 4 подобластей
            total = prefix[r1 + size][c1 + size] - prefix[r1][c1 + size] - prefix[r1 + size][c1] + prefix[r1][c1]
            # если они все нули или все единицы, возвращаем обобщающую вершину
            if total == 0:
                return Node(False, True, None, None, None, None)
            elif total == size * size:
                return Node(True, True, None, None, None, None)
            # в противном случае разбиваем область на вершины и повторяем алгоритм для них
            half = size // 2
            return Node(False, False,
                        build(r1, c1, half),
                        build(r1, c1 + half, half),
                        build(r1 + half, c1, half),
                        build(r1 + half, c1 + half, half))

        n = len(grid)

        # подсчет префиксной суммы, т.е. все единицы в области до [i, j] клетки
        # массив для этой суммы на 1 больше, чтобы можно было считать префикс на основании прошлых элементов
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                # значение в текущей клетке считается как значение добавленной клетки +
                # + значения прямоугольных областей перед этой клеткой минус общая часть
                prefix[i + 1][j + 1] = grid[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

        return build(0, 0, n)




if __name__ == '__main__':
    Solution().construct([[0,1],[1,0]])