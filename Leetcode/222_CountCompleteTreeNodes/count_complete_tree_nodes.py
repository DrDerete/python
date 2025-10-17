from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_height(self, root: Optional[TreeNode], left: bool) -> int:
        l = 0
        while root:
            l += 1
            root = root.left if left else root.right
        return l

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_length = self.get_height(root, True)
        right_length = self.get_height(root, False)
        if left_length == right_length:
            return 2 ** right_length - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == '__main__':
    print(Solution().countNodes(TreeNode(3, TreeNode(6))))
    print(Solution().countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))

