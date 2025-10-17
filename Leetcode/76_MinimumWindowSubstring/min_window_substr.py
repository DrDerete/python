from collections import defaultdict
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        # считаем сколько букв надо
        char_count = {}
        for ch in t:
            char_count[ch] = char_count.get(ch, 0) + 1
        # создаем окно
        begin = 0
        for end, ch in enumerate(s):
            # внутри которого считаем нужные символы
            if ch in char_count:
                char_count[ch] -= 1
                # если символов достаточно
                if all(val < 1 for val in char_count.values()):
                    loop = True
                    # удаляем лишние символы - двигаем левую сторону окна
                    while loop:
                        if s[begin] in char_count:
                                char_count[s[begin]] += 1
                                # добавляем символы пока не испортится условие
                                if char_count[s[begin]] > 0:
                                    loop = False
                        begin += 1
                    if ans == "":
                        ans = s[begin - 1:end + 1]
                    elif end - begin + 1 < len(ans):
                        ans = s[begin - 1: end + 1]
        return ans

    # можно сделать проверку оптимальней, добавив критерий по числу символов
    # то есть одной переменной и парой проверок заменяем проход по values в all
    def minWindow1(self, s: str, t: str) -> str:
        ans = ""
        char_count = dict(Counter(t))
        condition = len(t)
        begin = 0
        for end, ch1 in enumerate(s):
            if ch1 in char_count:
                if char_count[ch1] > 0:
                    condition -= 1
                char_count[ch1] -= 1
                if condition == 0:
                    while True:
                        ch2 = s[begin]
                        if ch2 in char_count:
                            char_count[ch2] += 1
                            if char_count[ch2] > 0:
                                condition += 1
                                break
                        begin += 1
                    if ans == "":
                        ans = s[begin:end + 1]
                    elif end - begin < len(ans):
                        ans = s[begin: end + 1]
                    begin += 1
        return ans

    # чей то пример с defaultdict(в отличие от обычной мапы не требует наличие ключа)
    def minWindow2(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        char_count = defaultdict(int)
        for ch in t:
            char_count[ch] += 1

        target_chars_remaining = len(t)
        min_window = (0, float("inf"))
        start_index = 0

        for end_index, ch in enumerate(s):
            if char_count[ch] > 0:
                target_chars_remaining -= 1
            char_count[ch] -= 1

            if target_chars_remaining == 0:
                while True:
                    char_at_start = s[start_index]
                    if char_count[char_at_start] == 0:
                        break
                    char_count[char_at_start] += 1
                    start_index += 1

                if end_index - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)

                char_count[s[start_index]] += 1
                target_chars_remaining += 1
                start_index += 1

        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1] + 1]








if __name__ == '__main__':
    print(Solution().minWindow("a", "aa"))
    print(Solution().minWindow("acaaccaacjhajcy", "abc"))
    print(Solution().minWindow("ADABECODEBAAC", "ABC"))
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    print(Solution().minWindow("a", "a"))
