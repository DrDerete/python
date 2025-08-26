class Solution(object):
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        last = None
        for num in s:
            if last is None:
                last = num
            else:
                if dict_nums[num] <= dict_nums[last]:
                    ans += dict_nums[last]
                    last = num
                else:
                    ans += dict_nums[num] - dict_nums[last]
                    last = None
        if last is not None:
            ans += dict_nums[last]
        return ans

    def romanToInt2(self, s):
        roman_dict = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        value = 0
        last_value = 0
        for char in reversed(s):
            value = roman_dict[char]
            if value < last_value:
                total -= value
            else:
                total += value
                last_value = value
        return total


if __name__ == '__main__':
    print(Solution().romanToInt2("III"))
    print(Solution().romanToInt2("LVIII"))
    print(Solution().romanToInt2("MCMXCIV"))
