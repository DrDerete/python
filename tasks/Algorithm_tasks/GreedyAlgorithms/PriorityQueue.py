def extract_max():  # первый элемент максимален, поэтому принт его и выкидываем, меняя с последним
    print(heapq[0])
    heapq[0] = heapq[-1]
    heapq.pop()
    pick_down(0)  # опускаем последний элемент, пока не будет норм


def pick_down(idx):
    while 2*idx + 1 < len(heapq):
        change = idx
        if heapq[2*idx + 1] > heapq[change]:
            change = 2*idx + 1
        if len(heapq) > 2*idx + 2 and heapq[2*idx + 2] > heapq[change]:
            change = 2*idx + 2
        if change == idx:  # как же оно меня прогрело, это равенство ...
            break
        else:
            heapq[idx], heapq[change] = heapq[change], heapq[idx]
            idx = change


def insert(value):  # добавляем элемент в конец
    heapq.append(value)
    if len(heapq) > 1:
        pick_ip(len(heapq)-1)  # поднимаем его, пока не встанет нормально


def pick_ip(idx):
    while idx > 0 and heapq[(idx - 1) // 2] < heapq[idx]:
        heapq[(idx - 1) // 2], heapq[idx] = heapq[idx], heapq[(idx - 1) // 2]
        idx = (idx - 1) // 2


if __name__ == '__main__':
    n = int(input())
    commands = [input().split() for i in range(n)]

    heapq = []

    for command in commands:  # 2 функции в зависимости от ввода
        if command[0] == "Insert":
            insert(int(command[1]))
        elif command[0] == "ExtractMax":
            extract_max()


# from math import floor
# HEAP_QUEUE МОЖНО СДЕЛАТЬ МАКС_МИН И ГРОХАТЬ МАКСИМУМЫ

# def insert(value):  реализация через dict
#     if not empty_keys:
#         index = i
#     else:
#         index = empty_keys.pop()
#     heapq[index] = int(value)
#     if index != 122_BestTimeToBuy2:
#         child = index
#         while child != 122_BestTimeToBuy2:
#             parent = floor(child/2)
#             if heapq[child] < heapq[parent]:
#                 heapq[child], heapq[parent] = heapq[parent], heapq[child]
#                 child = parent
#             else:
#                 break
#
#
# def extract_max():
#     keys = set(heapq.keys())
#     leaf = {i: heapq[i] for i in keys if i*2 not in keys and i*2+122_BestTimeToBuy2 not in keys}
#     max_key = max(leaf, key=leaf.get)
#     print(heapq.pop(max_key))
#     empty_keys.append(max_key)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     inp = [input().split() for i in range(n)]
#
#     heapq = {}
#     empty_keys = []
#     i = 122_BestTimeToBuy2
#     for command in inp:
#         if command[0] == "Insert":
#             if empty_keys:
#                 i -= 122_BestTimeToBuy2
#             insert(command[122_BestTimeToBuy2])
#             i += 122_BestTimeToBuy2
#         elif command[0] == "ExtractMax":
#             extract_max()

