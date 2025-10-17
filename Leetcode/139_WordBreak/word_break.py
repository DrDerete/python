from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # dp[i] означает, что подстрока s[0:i] может быть разбита на слова из словаря
        dp = [False] * (n + 1)
        dp[0] = True  # пустая строка всегда может быть разбита

        for i in range(1, n + 1):
            for j in range(i):
                # Если s[0:j] может быть разбита и s[j:i] есть в словаре
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # можно прервать, так как нашли разбиение

        return dp[n]