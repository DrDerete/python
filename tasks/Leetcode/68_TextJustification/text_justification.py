class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        max_str = []
        for word in words:
            max_str.append(word)
            # добавляем слово и поверяем хватает ли места на них и хотя бы 1 пробел между ними
            if sum(len(w) for w in max_str) + (len(max_str) - 1) > maxWidth:
                # если не хватает
                new = max_str.pop()  # запоминаем последнее слово
                cels = maxWidth - sum(len(w) for w in max_str)  # пробелы до maxWidth
                if len(max_str) == 1:  # если слово одно, то пробелы в конец
                    ans.append(max_str[0] + " " * cels)
                else:  # а так распрямляем по пробелам между словами
                    spaces = len(max_str) - 1  # кол-во пробелов
                    sep = " " * (cels // spaces)  # получается вот такой сепаратор
                    mod = cels % spaces  # но есть нюанс
                    for i in range(mod):  # добавляем пробелы к слову если mod > 0
                        max_str[i] += " "  # вот он зараза
                    ans.append(sep.join(max_str))
                max_str = [new]
        # записываем последнюю строку
        max_str = " ".join(max_str)
        cels = maxWidth - len(max_str)
        ans.append(max_str + " " * cels)
        return ans

    def fullJustify1(self, words, maxWidth):
        ret, line_words, line_len = [], [], 0

        for word in words:
            if line_len + len(word) + len(line_words) > maxWidth:  # need to justify current line
                spaces = maxWidth - sum(len(w) for w in line_words)
                if len(line_words) == 1:
                    ret.append(line_words[0] + " " * spaces)
                else:
                    even_spaces, extra = divmod(spaces, len(line_words) - 1)
                    line = ""
                    for i, w in enumerate(line_words):
                        line += w
                        if i < len(line_words) - 1:
                            line += " " * (even_spaces + (1 if i < extra else 0))
                    ret.append(line)
                line_words, line_len = [], 0
            line_words.append(word)
            line_len += len(word)

        # last line - left justified
        ret.append(" ".join(line_words).ljust(maxWidth))
        return ret


if __name__ == '__main__':
    print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(Solution().fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"], 16))
