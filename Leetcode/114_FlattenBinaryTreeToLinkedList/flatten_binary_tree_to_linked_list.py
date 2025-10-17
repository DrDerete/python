from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        preorder[-1].left = None
        preorder[-1].right = None

        for i in range(len(preorder) - 1):
            preorder[i].left = None
            preorder[i].right = preorder[i + 1]

        return None

    def flatten1(self, root):
        if not root:
            return None
        # идея в том, чтобы разворачивать дерево вправо
        current = root
        while current:
            # берем крайний правый узел в левом поддереве и переносим всё правое поддерево в его конец
            if current.left:
                # находим узел к которому надо присоединить правое поддерево
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                # соединяем и наслаждаемся
                predecessor.right = current.right
                current.right = current.left
                current.left = None
            # переходим к следующему узлу
            current = current.right
        return root



if __name__ == '__main__':
    Solution().flatten1(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))))

