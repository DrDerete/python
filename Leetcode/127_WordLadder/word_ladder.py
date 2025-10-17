from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 5% 99%
        bank = set(wordList)
        if endWord not in bank:
            return 0
        trans = deque([beginWord])
        step_trans = 1
        while trans:
            for _ in range(len(trans)):
                curr = trans.popleft()
                if curr == endWord:
                    return step_trans
                for word in list(bank):
                    dif_let = sum(1 for a, b in zip(curr, word) if a != b)
                    if dif_let == 1:
                        trans.append(word)
                        bank.remove(word)
            step_trans += 1
        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 99% 90-95%
        # такой выйгрыш в скорости достигается за счет двунаправленного обхода - идем со стороны где меньше слов,
        # а также за счет ручной трансформации букв - не сравниваем каждое с каждым(N * N), а трансформируем буквы (N * 26)
        s = set(wordList)
        if endWord not in s:
            return 0
        if beginWord == endWord:
            return 1
        frontBegin, frontEnd = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        d = 1
        while frontBegin and frontEnd:
            if len(frontBegin) > len(frontEnd):
                frontBegin, frontEnd = frontEnd, frontBegin
            nxt = set()
            d += 1
            for w in frontBegin:
                wlst = list(w)
                for i in range(len(wlst)):
                    orig = wlst[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == orig:
                            continue
                        wlst[i] = c
                        t = ''.join(wlst)
                        if t in frontEnd:
                            return d
                        if t in s and t not in visited:
                            visited.add(t)
                            nxt.add(t)
                    wlst[i] = orig
            frontBegin = nxt
        return 0


    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # попробовал повторить, нраится
        bank = set(wordList)
        if endWord not in bank:
            return 0
        if beginWord == endWord:
            return 1

        from_begin = {beginWord}
        from_end = {endWord}

        word_len = len(beginWord)
        ans = 1

        while from_begin and from_end:
            if len(from_begin) > len(from_end):
                from_begin, from_end = from_end, from_begin
            next_words = set()
            ans += 1

            for word in from_begin:
                for i in range(word_len):
                    word_list = list(word)
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word_list[i]:
                            continue
                        word_list[i] = ch
                        trans_word = "".join(word_list)

                        if trans_word in from_end:
                            return ans

                        if trans_word in bank:
                            next_words.add(trans_word)
                            bank.remove(trans_word)
            from_begin = next_words
        return 0


if __name__ == '__main__':
    Solution().ladderLength2("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
    Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
