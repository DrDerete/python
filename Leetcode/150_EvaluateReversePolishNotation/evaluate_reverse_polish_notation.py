from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                last = stack.pop()
                if t == "+":
                    stack[-1] += last
                elif t == "-":
                    stack[-1] -= last
                elif t == "*":
                    stack[-1] *= last
                elif t == "/":
                    stack[-1] = int(stack[-1] / last)
        return stack[0]


if __name__ == '__main__':
    print(Solution().evalRPN(["2","1","+","3","*"]))
    print(Solution().evalRPN(["4","13","5","/","+"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
