def word_in_line(words, digits):  # количество слов в строку с ограничением по количеству символов
    length = 0
    c = 0
    for word in words:
        if length + c + len(word) > digits:
            return length + c - 1
        length += len(word)
        if length + 1 > digits - c:
            return length + c
        c += 1
    return length + c - 1
