class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = ""
        ans = 0
        for ch in s:
            if ch in uniq:
                if len(uniq) > ans:
                    ans = len(uniq)
                uniq = uniq.partition(ch)[2]
                # uniq = uniq[uniq.find(ch) + 1:]
            uniq += ch
        if len(uniq) > ans:
            ans = len(uniq)
        return ans

    def lengthOfLongestSubstring1(self, s: str) -> int:
        seen = set()
        # индекс для удаления элементов из set
        # идем по изначальной строке и удаляем элементы
        # но надо постоянно проверять удалён ли нужный элемент
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        start = -1
        max = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i - start > max:
                    max = i - start
        return max


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring2("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("p"))
