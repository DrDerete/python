from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # проходим в inorder порядке и находим k-ый элемент
        self.i = 0
        self.ans = None
        def inorder(node):
            if node.left:
                inorder(node.left)
            self.i += 1
            if self.i == k:
                self.ans = node.val
            if self.ans:
                return
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.ans


if __name__ == '__main__':
    Solution().kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1)

