from typing import List

class Solution:
    #  "" -> ( -> (( () -> (() ()( -> (()) ()()

    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
        result = []
        backtrack("", 0, 0)
        return result

    def generateParenthesis1(self, n: int) -> List[str]:
        state = [("", 0, 0)]
        for _ in range(n * 2):
            next_state = []
            for s, open_p, closed_p in state:
                if open_p < n:
                    next_state.append((s+"(", open_p + 1, closed_p))
                if open_p > closed_p:
                    next_state.append((s+")", open_p, closed_p + 1))
            state = next_state
        return [s[0] for s in state]

if __name__ == '__main__':
    Solution().generateParenthesis1(4)
    Solution().generateParenthesis(2)
