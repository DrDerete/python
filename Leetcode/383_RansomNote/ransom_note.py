from collections import defaultdict
from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        checker = dict(Counter(ransomNote))
        for ch in magazine:
            if ch in checker:
                checker[ch] -= 1
                if checker[ch] == 0:
                    checker.pop(ch)
                    if not checker:
                        return True
        return False

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        for ch in set(ransomNote):
            if ransomNote.count(ch)>magazine.count(ch): return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for cRansomNote in ransomNote:
            if not cRansomNote in magazine:
                return False
            else:
                magazine = magazine.replace(cRansomNote, " ", 1)
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = defaultdict(int)
        for c in magazine:
            magazine_map[c] += 1
        for ran_char in ransomNote:
            if magazine_map[ran_char] <= 0:
                return False
            magazine_map[ran_char] -= 1
        return True

if __name__ == '__main__':
    print(Solution().canConstruct("a", "b"))
    print(Solution().canConstruct("aa", "aab"))