from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iter_order = [TreeNode(-1)]
        def dfs(node):
            if node.left:
                dfs(node.left)
            self.iter_order.append(node)
            if node.right:
                dfs(node.right)
        dfs(root)
        self.idx = 0

    def next(self) -> int:
        self.idx += 1
        return self.iter_order[self.idx].val

    def hasNext(self) -> bool:
        return self.idx < len(self.iter_order)


class BSTIterator1:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == '__main__':
    inp = TreeNode(7, TreeNode(3, TreeNode(15, TreeNode(9))))
    ob = BSTIterator(inp)
    ob.hasNext()
    ob.next()
    ob.next()
    ob.next()
    ob.hasNext()
