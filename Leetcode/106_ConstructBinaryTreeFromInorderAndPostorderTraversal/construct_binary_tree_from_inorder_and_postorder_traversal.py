from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # принципиальным прямым обходом было решено ;]
        if not inorder:
            return None
        root = TreeNode(inorder[0])
        stack = [root]
        post_idx = 0
        for i in range(1, len(inorder)):
            node = TreeNode(inorder[i])
            child = None

            while stack and stack[-1].val == postorder[post_idx]:
                save = child
                child = stack.pop()
                post_idx += 1
                if save:
                    child.right = save

            if child:
                node.left = child
            stack.append(node)

        root = stack[0]
        head = root
        for i in range(1, len(stack)):
            head.right = stack[i]
            head = head.right

        return root

    def buildTree1(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)

        root.left = self.buildTree1(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree1(inorder[root_index + 1:], postorder[root_index:-1])

        return root

    def buildTree2(self, inorder, postorder):
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_index = len(inorder) - 1

        for i in range(len(postorder) - 2, -1, -1):
            node = TreeNode(postorder[i])
            parent = None

            while stack and stack[-1].val == inorder[inorder_index]:
                parent = stack.pop()
                inorder_index -= 1

            if parent:
                parent.left = node
            else:
                stack[-1].right = node
            stack.append(node)

        return root

if __name__ == '__main__':
    Solution().buildTree([1,2,3,4], [2,3,1,4])
    Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
    Solution().buildTree([20,11,9,2,3,7], [20,11,2,9,7,3])
    Solution().buildTree([1,2,3,4,5], [5,4,3,2,1])
    Solution().buildTree([5,4,3,2,1], [5,4,3,2,1])
