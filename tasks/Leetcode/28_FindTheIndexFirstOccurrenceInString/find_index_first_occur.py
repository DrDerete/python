class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStr1(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr1("sadbutsad", "sad"))
