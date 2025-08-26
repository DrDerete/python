def count_components():
    components = []  # тут считаем компоненты связности
    for elem in graf.keys():
        if elem in set().union(*components):  # если вершина связна, пропускаем
            continue
        components.append(get_component(elem))  # обновляем список связных вершин
    return len(components)


def get_component(begin, visited=None):
    if visited is None:
        visited = set()
    visited.add(begin)  # запоминаем откуда пришли
    if len(graf[begin]) == 0:
        return visited  # если идти некуда заканчиваем
    else:
        ways = [elem for elem in graf[begin] if elem not in visited]  # в противном случае проходим по всем доступным вершинам
        for i in ways:
            visited = get_component(i, visited)  # не забываем список посещенных вершин передать и вернуть
        return visited


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    edges = [[int(x) for x in input().split()] for i in range(inp[1])]  # массив ребер графа
    edges = [elem for elem in edges if len(set(elem)) == 2]  # удаление ребер петель
    graf = {i: [sum(elem)-i for elem in edges if i in elem] for i in range(1, inp[0]+1)}  # удобная структура представления графа {вершина: [список связных вершин]}
    print(count_components())
