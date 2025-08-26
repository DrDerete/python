def count_sort(arr):  # тут всё прям по лекции
    counter = [0 for i in range(max(arr)+1)]  # массив нулей по максимальному элементу
    for x in arr:
        counter[x] += 1  # считаем сколько и каких элементов встретилось
    for i in range(2, len(counter)):
        counter[i] += counter[i-1]  # накапливаем количество элементов, тем самым получая индексы, на которых должны стоять отсортированные элементы основного массива
    sorter = [0 for i in range(len(arr))]  # остается создать массив в который переписать элементы
    for j in reversed(range(len(arr))):
        sorter[counter[arr[j]]-1] = arr[j]  # сортированный[куда[кого]] = ставим
        counter[arr[j]] -= 1  # изменяем индекс на
    return sorter


if __name__ == '__main__':  # эффективность определяется максимумом значений в массиве
    n = int(input())
    inp = [int(x) for x in input().split()]

    print(*count_sort(inp))
