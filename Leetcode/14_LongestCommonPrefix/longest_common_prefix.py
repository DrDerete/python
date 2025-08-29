class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        i = 0
        common = True
        while common:
            char = None
            for string in strs:
                if i > len(string) - 1:
                    common = False
                    break
                if char is None:
                    char = string[i]
                if char != string[i]:
                    common = False
                    break
            if common:
                i += 1
                ans += char
        return ans

    def longestCommonPrefix1(self, strs):
        string = strs[0]
        for i in range(len(string)):
            for s in strs[1:]:
                if i > len(s) - 1:
                    return string[:i]
                if s[i] != string[i]:
                    return string[:i]
        return string

    def longestCommonPrefix2(self, strs):
        prefix = ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            current_char = shortest[i]
            for word in strs:
                if word[i] != current_char:
                    return prefix
            prefix += current_char
        return prefix


if __name__ == '__main__':
    print(Solution().longestCommonPrefix1(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix1(["dog", "racecar"," car"]))
    print(Solution().longestCommonPrefix1(["dog", "dog_gof", "dogs"]))
