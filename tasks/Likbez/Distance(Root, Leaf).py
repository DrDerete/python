from collections import deque


def distance(roots):
    distances = {roots[0]: 0}  # считаем дистанцию с помощью списка
    queue = deque(roots[0])

    while queue:  # пока в списке есть соседние вершины
        current = queue.popleft()   # удаляем первую
        cur_dist = distances[current]  # фиксируем дистанцию удаления от корня

        for neighbor in graf[current]:  # отмечаем соседей и добавляем их в список на проверку
            if neighbor not in distances:
                distances[neighbor] = cur_dist + 1
                queue.append(neighbor)

    return " ".join(str(distances[i]) for i in range(len(distances)))


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    edges = [[int(x) for x in input().split()] for i in range(inp[1])]
    graf = {i: set() for i in range(inp[0])}
    for u, v in edges:  # заполнение графа по учебнику
        graf[u].add(v)
        graf[v].add(u)

    print(distance([0]))
