def find_and_remove():  # обновление в очереди
    left = min(elements, key=lambda key: elements[key])
    val1 = elements.pop(left)
    right = min(elements, key=lambda key: elements[key])
    val2 = elements.pop(right)
    return [left, right, val1 + val2]


def encoding():  # кодирование входной строки
    answer = ""
    for ltr in inp:
        answer += to_string(coder[ltr])
    return answer


def to_string(lst):  # массив в строку(с конца)
    ans = ""
    for j in range(len(lst)-1, -1, -1):
        ans += str(lst[j])
    return ans


if __name__ == '__main__':
    inp = input()
    elements = {x: 0 for x in set(inp)}  # подсчет частот
    for ch in inp:
        elements[ch] += 1

    coder = {key: [] for key in elements}  # структура для кодирования

    if len(coder) < 3:  # обработка маленького кол-тва символов
        i = 0
        for key in coder:
            coder[key] = [i]
            i += 1
    else:
        while len(elements) != 1:  # алгоритм хоффмана и создание coder
            wood_h = find_and_remove()
            elements[wood_h[0] + wood_h[1]] = wood_h[2]
            for ch in wood_h[0]:
                coder[ch].append(0)
            for ch in wood_h[1]:
                coder[ch].append(1)

    code = encoding()

    print(f"{len(coder)} {len(code)}")
    for key in coder:
        print(f"{key}: {to_string(coder[key])}")
    print(code)
