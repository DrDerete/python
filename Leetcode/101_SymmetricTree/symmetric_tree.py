from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # увидел что это комбинация прошлых
        def invertTree(tree: Optional[TreeNode]) -> Optional[TreeNode]:
            if tree:
                tree.left, tree.right = invertTree(tree.right), invertTree(tree.left)
            return tree

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None or q is None: return p == q
            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        left = root.left
        right = invertTree(root.right)
        return isSameTree(left, right)


    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def symm(leftt, rightt):

            if not leftt or not rightt:
                return leftt == rightt
            if leftt.val != rightt.val: return False
            return symm(leftt.left, rightt.right) and symm(leftt.right, rightt.left)

        val = symm(root.left, root.right)
        return val

