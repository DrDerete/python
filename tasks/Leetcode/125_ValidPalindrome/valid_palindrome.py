from string import punctuation


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 70% 90%
        beg, end = 0, len(s) - 1
        while beg < end:
            if not s[beg].isalnum():
                beg += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[beg].lower() != s[end].lower():
                return False
            else:
                beg += 1
                end -= 1
        return True

    def isPalindrome1(self, s):
        # 90% 70%
        def isPalindrome1(self, s):
            s = s.lower().replace(" ", "")
            for i in punctuation:
                s = s.replace(i, "")
            return True if s[::-1] == s else False

    def isPalindrome2(self, s):
        # вот это круто
        x = ''.join(c for c in s if c.isalnum()).lower()
        return x == x[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome(" "))
    print(Solution().isPalindrome(".,"))

