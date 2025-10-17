from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        self.previous = None
        def inorder(node):
            if node.left:
                inorder(node.left)
            if self.valid:
                if self.previous is not None:
                    if self.previous >= node.val:
                        self.valid = False
                        return
                self.previous = node.val
                if node.right:
                    inorder(node.right)
        inorder(root)
        return self.valid
