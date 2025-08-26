class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # это работает
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        forward = True
        shift = 0
        for i in range(len(s)):
            if forward:
                ans[(i - shift) % numRows].append(s[i])
                if (i - shift) % numRows == numRows - 1:
                    forward = False
            else:
                ans[numRows - (i % (numRows + numRows - 2) + 2)].append(s[i])
                shift += 1
                if numRows - (i % (numRows + numRows - 2) + 2) == 1 - numRows:
                    forward = True
        return "".join(["".join(arr) for arr in ans])

    def convert1(self, s, numRows):
        # а это идеальный вариант
        if numRows == 1 or numRows >= len(s):
            return s

        ans = [""] * numRows
        cur_row = 0
        going_down = False

        for ch in s:
            ans[cur_row] += ch
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return "".join(ans)


if __name__ == '__main__':
    print(Solution().convert1("AB", 1))
    print(Solution().convert1("PAYPALISHIRING", 4))
    print(Solution().convert1("PAYPALISHIRING", 3))
    print(Solution().convert1("A", 1))
