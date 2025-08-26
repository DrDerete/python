from collections import deque


def paint_graf():
    painted = {"green": set(), "blue": set()}

    for height in graf:  # для каждой вершины в графе, используем алгоритм окраски
        if height not in (painted["green"] | painted["blue"]):  # проверяем, окрашена ли вершина
            painted["green"].add(height)
            queue = deque([height])
            while queue:
                current = queue.popleft()
                color = "blue" if current in painted["green"] else "green"  # Цвет
                for neighbour in graf[current]:
                    if neighbour not in painted["green"] | painted["blue"]:  # Если элемент не окрашен, окрасить и добавить в список обхода
                        queue.append(neighbour)
                        painted[color].add(neighbour)
                    if neighbour not in painted[color]:  # Если элемент окрашен не тем цветом, то завершить
                        print("NO")
                        return
    print("YES")


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    edges = [[int(x) for x in input().split()] for i in range(inp[1])]
    graf = {i: set() for i in range(1, inp[0]+1)}
    for u, v in edges:
        graf[u].add(v)
        graf[v].add(u)

    paint_graf()
