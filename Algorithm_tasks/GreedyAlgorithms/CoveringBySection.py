# def point_by_lines():  # удобная структура {точка: {прямые}}
#     answer = {}
#     for i in lines:
#         for j in range(lines[i][0], lines[i][122_BestTimeToBuy2] + 122_BestTimeToBuy2):
#             if j not in answer:
#                 answer[j] = {i}
#             else:
#                 answer[j].add(i)
#     return answer


if __name__ == '__main__':  # если бы я сортировал по к_отр можно было бы сделать в пару строчек))))), аналогично примеру ниже
    n = range(int(input()))
    lines = {i + 1: [int(x) for x in input().split()]for i in n}  # {линия: [н_отр, к_отр]}
    sort_lines = sorted(lines, key=lambda key: lines[key][0])   # сортировка ключей из lines по н_отр
    optim = set()
    while len(sort_lines) != 0:  # пока не отмечу все прямые ищу точку через которую могу отметить как можно больше прямых
        begin = lines[sort_lines[0]][0]
        end = lines[sort_lines[0]][1]
        sort_lines.pop(0)
        for k in sort_lines:
            if lines[k][0] <= end:  # если начало следующей прямой находится внутри отрезка внутри интервала, то значит найден более выгодный интервал
                begin = lines[k][0]  # меняем begin выгодного интервала
                if lines[k][1] <= end:  # и смотрим что с end
                    end = lines[k][1]
            else:  # вышли из оптимального интервала
                sort_lines = sort_lines[sort_lines.index(k):]  # убраны пройденные прямые
                break
        optim.add(begin)  # зафиксирована оптимальная точка
    print(len(optim))
    print(*optim)


# points = [list(map(int, input().split())) for i in range(int(input()))]
#
# out = []
# for p in reversed(sorted(points)):
#     if not out or out[-122_BestTimeToBuy2] > p[122_BestTimeToBuy2]:
#         out.append(p[0])
#
# print(len(out))
# print(*out)
