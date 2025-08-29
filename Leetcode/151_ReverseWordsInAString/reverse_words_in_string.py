class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # inline экономия памяти
        ans = s.split()
        ans.reverse()
        return " ".join(ans)

    def reverseWords1(self, s):
        ans = s.strip().split()
        return " ".join(ans[::-1])

    def _reverseWords2(self, s):
        words = s.split()
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)


if __name__ == '__main__':
    print(Solution().reverseWords("  hello world  "))
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("a good   example"))

