class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        char_word = {}
        for i in range(len(pattern)):
            if pattern[i] in char_word:
                if char_word[pattern[i]] != s[i]:
                    return False
                else:
                    char_word[pattern[i]] = s[i]
            else:
                if s[i] in char_word.values():
                    return False
                char_word[pattern[i]] = s[i]
        return  True


if __name__ == '__main__':
    print(Solution().wordPattern("abba", "dog cat cat dog"))