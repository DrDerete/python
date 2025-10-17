from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if node.right or node.left:
                if node.left:
                    stack.append((node.left, val * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, val * 10 + node.right.val))
            else:
                ans += val
        return ans

    def sumNumbers1(self, root):
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)

if __name__ == '__main__':
    Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3)))