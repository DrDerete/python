from typing import List, Counter

class Solution:
    #  лучшее по памяти
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        word_len, word_count = len(words[0]), len(words)
        subword_len = word_len * word_count
        if subword_len > len(s):
            return ans
        checker = dict(Counter(words))
        # первая идея - считать слова с обработкой исключений
        for i in range(len(s) - subword_len + 1):
            seen = {}
            for j in range(i, i + subword_len, word_len):
                word = s[j:j+word_len]
                # если слова нет
                if word not in checker:
                    break
                seen[word] = seen.get(word, 0) + 1
                # если слов слишком много
                if seen[word] > checker[word]:
                    break
            else:
                ans.append(i)
        return ans

    # дальше пытался придумать как можно изменять счётчик, чтобы по порядку найти все решения

    def findSubstring1(self, s, words):
        # в конце концов чтобы это корректно работало, нужно добавлять поверки
        # на возможность сдвига i или еще один цикл, а кода и так слишком много
        # через while i <= len(s) - subword_len я сдаюсь

        ans = []
        word_len, word_count = len(words[0]), len(words)
        subword_len = word_len * word_count
        if subword_len > len(s):
            return ans

        checker = {}
        for word in words:
            checker[word] = checker.get(word, 0) + 1

        i = 0
        while i <= len(s) - subword_len:
            seen_words = {}
            for j in range(i, i + subword_len, word_len):
                target_words = checker.keys()
                for k in range(word_len):
                    target_words = [w for w in target_words if w[k] == s[j + k]]
                    if not target_words: break
                else:
                    word = target_words[0]
                    if word in seen_words:
                        if seen_words[word][1] < checker[word]:
                            seen_words[word][1] += 1
                        else:
                            i = seen_words[word][0]
                            break
                    else:
                        seen_words[word] = [j + word_len, 1]
                if not target_words:
                    i = j + 1
                    break
            else:
                ans.append(i)
                i += word_len
        return ans

    # На этом моменте стало понятно, что буква пропускается, если она не является
    # частью какого-то слова, в противном изменять i без проверок нельзя, но вот что можно?
    # А можно использовать такой цикл, что проверки и не понадобятся. А именно
    # запускаем обычный цикл по word_length, но из разных начальных позиций, чтобы
    # пройти все подстроки


    # лучшее по скорости
    def findSubstring2(self, s, words):
        word_len, word_count = len(words[0]), len(words)
        subword_len = word_len * word_count
        check = dict(Counter(words))
        ans = []
        for i in range(word_len):
            # из разных позиций
            seen_words = {}
            left, right = i, i
            while left <= len(s) - subword_len:
                # добавляем слова и проверяем
                right += word_len
                word = s[right - word_len:right]
                if word in check:
                    # если слово в словаре
                    seen_words[word] = seen_words.get(word, 0) + 1
                    while seen_words[word] > check[word]:
                        # если слов больше, то удаляем лишние
                        seen_words[s[left:left + word_len]] -= 1
                        left += word_len
                    if right - left == subword_len:
                        # если набрался ответ
                        ans.append(left)
                else:
                    # если слова нет
                    left = right
                    seen_words.clear()
        return ans

    def findSubstring3(self, s, words):
        if not words:
            return []

        hashmap = {}
        target_valid_count = 0
        for word in words:
            target_valid_count += 1
            hashmap[word] = hashmap.get(word, 0) + 1
        length = len(words[0])

        result = []
        cur_hashmap = {}
        L = 0
        for i in range(length):
            cur_hashmap.clear()
            valid_count = 0
            L = i

            valid_count = 0
            for R in range(i, len(s), length):
                new_word = s[R:R + length]
                if new_word not in hashmap:
                    L = R + length
                    valid_count = 0
                    cur_hashmap.clear()
                else:
                    cur_hashmap[new_word] = cur_hashmap.get(new_word, 0) + 1
                    if cur_hashmap[new_word] <= hashmap[new_word]:
                        valid_count += 1
                    else:
                        while cur_hashmap[new_word] > hashmap[new_word]:
                            left_word = s[L:L + length]
                            cur_hashmap[left_word] -= 1
                            L += length
                            if left_word != new_word:
                                valid_count -= 1
                    if valid_count == target_valid_count:
                        result.append(L)

        return result


if __name__ == '__main__':
    print(Solution().findSubstring2("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
    print(Solution().findSubstring2("barfoothefoobarman", ["foo","bar"]))
    print(Solution().findSubstring2("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(Solution().findSubstring2("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(Solution().findSubstring2("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(Solution().findSubstring2("barfoofoobarthefoobarman", ["bar","foo","the"]))
