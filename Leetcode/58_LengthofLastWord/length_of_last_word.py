class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = True
        length = 0
        for ch in s:
            if ch == " ":
                last = False
            else:
                if last:
                    length += 1
                else:
                    last = True
                    length = 1
        return length

    def lengthOfLastWord1(self, s):
        word = s.strip().split()
        return len(word[-1])


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
