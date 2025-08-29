# Можно было бы реализовать просто через сравнение входной строки с dict алфавита, но ... Я ТАК ВИЖУ
def create_decoder():
    inp_d = {x[0]: [int(x[1][i]) for i in range(len(x[1])-1, -1, -1)] for x in inp}
    root = {}  # создание директории, вида {имя вершины: [левый ветвь, правая ветвь]}
    que = ["".join(inp_d.keys())]
    while len(que) != 0:  # тут через очередь сделано наполнение директории root
        parent = que.pop(0)
        child = ["", ""]
        for ch in parent:
            if inp_d[ch].pop() == 0:
                child[0] += ch
            else:
                child[1] += ch
        root[parent] = child  # вершина и дети
        for elem in child:  # если дети не листы, повторяем алгоритм уже для них
            if len(elem) > 1:
                que.append(elem)
    return root


def decode_mess():  # декодируем сообщение
    line_e = [int(line[i]) for i in range(len(line)-1, -1, -1)]  # строка декодирования, для удобства с конца
    root = "".join([x[0] for x in inp])  # корень дерева
    message = ""
    while len(line_e) != 0:
        key = root  # для каждого символа в строке, идем по псевдо-дереву декодирования
        while True:
            ch = line_e.pop()
            if len(decoder[key][ch]) == 1:  # дошли до буквы и записываем ответ
                message += decoder[key][ch]
                break
            else:  # идем дальше
                key = decoder[key][ch]
    return message


if __name__ == '__main__':
    ltrs, bits = [int(x) for x in input().split()]
    inp = [input().split(": ") for i in range(ltrs)]
    line = input()

    decoder = create_decoder()  # получили директорию, "псевдо-дерево" декодирования

    print(decode_mess())  # принт сообщения



