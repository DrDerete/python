class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        int_n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_n = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        while num:
            for _ in range(num // int_n[i]):
                ans += roman_n[i]
                num -= int_n[i]
            i += 1
        return ans

    def intToRoman1(self, num):
        val_to_roman = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        result = []
        for value, symbol in val_to_roman:
            while num >= value:
                result.append(symbol)
                num -= value
        return ''.join(result)

    def intToRoman2(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
                M[num // 1000] +
                C[(num % 1000) // 100] +
                X[(num % 100) // 10] +
                I[num % 10]
        )


if __name__ == '__main__':
    print(Solution().intToRoman(3749))
