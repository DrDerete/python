class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False

    def isSubsequence1(self, s, t):
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        pointer = 0
        for x in t:
            if s[pointer] == x:
                pointer += 1
            if pointer == len(s):
                return True
        return False

    def isSubsequence2(self, s, t):
        iterate = iter(t)
        return all(char in iterate for char in s)


if __name__ == '__main__':
    print(Solution().isSubsequence2("abc", "ahbgdc"))
    print(Solution().isSubsequence2("axc", "ahbgdc"))
