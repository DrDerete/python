from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_l = self.maxDepth(root.left)
        l_r = self.maxDepth(root.right)
        return max(l_l, l_r) + 1

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth1(root.left), self.maxDepth1(root.right)) + 1



if __name__ == '__main__':
    Solution().maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))