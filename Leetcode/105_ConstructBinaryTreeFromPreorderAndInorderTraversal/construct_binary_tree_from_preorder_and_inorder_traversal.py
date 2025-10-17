from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0

        for i in range(1, len(preorder)):
            # каждый элемент массива это вершина дерева
            node = TreeNode(preorder[i])
            parent = None
            # если вершина относится к предыдущим, то следуя стеку будет найден родитель
            while stack and stack[-1].val == inorder[inorder_idx]:
                parent = stack.pop()
                inorder_idx += 1
            # присоединяем вершину
            if parent:
                parent.right = node
            else:
                stack[-1].left = node
            stack.append(node)

        return root

    def buildTree1(self, preorder, inorder):
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        # Находим индекс корня в inorder
        root_index = inorder.index(root_val)

        # Строим левое и правое поддеревья
        root.left = self.buildTree1(preorder[1:1 + root_index], inorder[:root_index])
        root.right = self.buildTree1(preorder[1 + root_index:], inorder[root_index + 1:])

        return root

if __name__ == '__main__':
    Solution().buildTree([1,2,3,4,5,6,7], [2,4,6,5,3,1,7])
    Solution().buildTree([3,1,2,4], [1,4,2,3])
    Solution().buildTree([3,1,2,4], [1,2,3,4])
    Solution().buildTree([1, 2, 3], [2, 3, 1])
    Solution().buildTree([1, 2, 3], [1, 2, 3])
    Solution().buildTree([1, 2, 3], [1, 3, 2])
    Solution().buildTree([1, 2, 3, 4, 5], [3, 2, 5, 4, 1])
    Solution().buildTree([1, 2, 3, 4, 5], [3, 2, 1, 5, 4])
    Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    Solution().buildTree([-1], [-1])
