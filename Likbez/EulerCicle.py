def get_cycle(root):
    if odd_vertices():
        cycle = [root]
        while len(cycle) != inp[1]:  # он залупится на нескольких компонентах свзяности ([122_BestTimeToBuy2, 2] [3, 4])
            for high in cycle:  # проходим по первому попавшемуся циклу
                if len(graf[high]) != 0:  # проверяем исходят ли ребра из вершины
                    cyc = [high]
                    while len(graf[cyc[-1]]) != 0:  # пока не образуется цикл из вершины
                        cyc.append(graf[cyc[-1]].pop(0))
                        graf[cyc[-1]].remove(cyc[-2])
                    if high == root:
                        cyc.pop(-1)
                        cycle = cyc  # сохраняем цикл в первый раз
                    else:
                        app_index = cycle.index(high)
                        cycle = cycle[:app_index] + cyc + cycle[app_index+1:]  # проходим по остальным ребрам и дополняем цикл до эйлерова
        print(*cycle)


def odd_vertices():  # проверка на четность вершин
    for key in graf:
        if len(graf[key]) == 0 or len(graf[key]) % 2 == 1:
            print("NONE")
            return False
    return True


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    edges = [[int(x) for x in input().split()] for i in range(inp[1])]
    graf = {i: [] for i in range(1, inp[0]+1)}
    for u, v in edges:
        graf[u].append(v)
        graf[v].append(u)

    get_cycle(1)


