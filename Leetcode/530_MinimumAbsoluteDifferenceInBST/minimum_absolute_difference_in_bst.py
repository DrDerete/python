from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        self.min_dif = 1000000

    # слева находятся меньшие, а справа большие узлы
    # значить надо спуститься сначала в самую левую ветку,
    # а потом из неё подниматься переходя вправо
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def count_df(node):
            # не спускаемся в None
            if node.left:
                count_df(node.left)
            # проверка на предыдущий по значению элемент
            if self.prev is not None:
                self.min_dif = min(self.min_dif, node.val - self.prev)
            # устанавливаем предыдущий элемент
            self.prev = node.val
            # далее
            # либо идем вправо (элемент больший чем текущий и там спускаемся снова влево,
            # т.е. Смотрим на меньший из бОльших элементов)
            # либо поднимаемся выше -- Это easy ? [-_-]
            if node.right:
                count_df(node.right)
        count_df(root)
        return self.min_dif

    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        # ну или inorder и сохраняем возрастание
        arr = []
        def dfs(root, arr):
            if not root:
                return
            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)
        dfs(root, arr)
        minn = arr[1] - arr[0]
        n = len(arr)
        for i in range(n - 1, 0, -1):
            minn = min(minn, arr[i] - arr[i - 1])
        return minn



if __name__ == '__main__':
    Solution().getMinimumDifference(TreeNode(100000, TreeNode(0)))
    Solution().getMinimumDifference(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)))
