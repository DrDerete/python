class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(": ")", "[": "]", "{": "}"}
        opened = []
        for ch in s:
            if ch in parentheses:
                opened.append(ch)
            else:
                if not opened:
                    return False
                if ch != parentheses[opened[-1]]:
                    return False
                opened.pop()
        return not opened

if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("([])"))
    print(Solution().isValid("([)]"))




