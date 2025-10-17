class Solution:
    def calculate(self, s: str) -> int:
        count_stack = [[0, 1]]
        brace, i = 0, 0
        while i < len(s):
            match s[i]:
                case " ":
                    pass
                case "(":
                    count_stack.append([0, 1])
                    brace += 1
                case ")":
                    expression_val = count_stack.pop()[0]
                    brace -= 1
                    count_stack[brace][0] += expression_val * count_stack[brace][1]
                case "+":
                    count_stack[brace][1] = 1
                case "-":
                    count_stack[brace][1] = -1
                case _:
                    number = ""
                    while i < len(s) and s[i].isdigit():
                        number += s[i]
                        i += 1
                    count_stack[brace][0] += int(number) * count_stack[brace][1]
                    continue
            i += 1
        return count_stack[0][0]

    def calculate1(self, s: str) -> int:
        stack = []
        total = 0
        sign = 1
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                total += sign * num
                i = j
                continue
            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append((total, sign))
                total = 0
                sign = 1
            elif char == ')':
                prev_total, prev_sign = stack.pop()
                total = prev_total + prev_sign * total
            i += 1
        return total

    def calculate2(self, s: str) -> int:
        stack = []
        cur_num = 0
        res = 0
        sign = 1
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '+':
                res += sign * cur_num
                sign = 1
                cur_num = 0
            elif c == '-':
                res += sign * cur_num
                sign = -1
                cur_num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * cur_num
                res *= stack.pop()
                res += stack.pop()
                cur_num = 0
        return res + cur_num * sign

if __name__ == '__main__':
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
    print(Solution().calculate("123421351"))
    print(Solution().calculate("1-11"))
    print(Solution().calculate("1+1"))
    print(Solution().calculate("1 + 3 + 7"))
