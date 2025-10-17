from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        w1 = dict(Counter(s))
        w2 = dict(Counter(t))
        return w1 == w2

if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("rat", "car"))