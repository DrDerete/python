from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        stack = []
        node = root
        last_visited = None
        branch_sums = {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    node = peek_node.right
                else:
                    stack.pop()
                    last_visited = peek_node
                    left_max = max(branch_sums.get(peek_node.left, 0), 0)
                    right_max = max(branch_sums.get(peek_node.right, 0), 0)
                    path_through_node = peek_node.val + left_max + right_max
                    max_sum = max(max_sum, path_through_node)
                    branch_sums[peek_node] = peek_node.val + max(left_max, right_max)

        return max_sum

    def maxPathSum1(self, root: Optional[TreeNode]) -> int:
        self.ans = -1100
        # адекватная рекурсия
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # максимумы левых и правых путей из узла
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            # проверяем локальный максимум
            self.ans = max(self.ans, left_max + right_max + node.val)
            return max(right_max, left_max) + node.val
        dfs(root)
        return self.ans






if __name__ == '__main__':
    Solution().maxPathSum(TreeNode(-10, TreeNode(1, TreeNode(5), TreeNode(20)), TreeNode(20, TreeNode(15), TreeNode(7))))
    Solution().maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3)))
    Solution().maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    Solution().maxPathSum(TreeNode(-10, TreeNode(50), TreeNode(20, TreeNode(15), TreeNode(7))))
