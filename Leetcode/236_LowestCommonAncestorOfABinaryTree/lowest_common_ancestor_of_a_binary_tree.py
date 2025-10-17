class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # 98% по памяти
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # волевой прямой проход, наролял 95% 99.5%
        stack = [root]
        way_p = None if p != root else [root]
        way_q = None if q != root else [root]
        visited = set()
        while not way_p or not way_q:
            # по условию задачи p и q гарантированно существуют
            change = False
            if root.left and root.left not in visited:
                # bool, чтобы отделить обработку проверки
                change = True
                root = root.left
                stack.append(root)
            elif root.right and root.right not in visited:
                change = True
                root = root.right
                stack.append(root)
            if change:
                # копируем если нашли нужную вершину
                if stack[-1] == p:
                    way_p = stack.copy()
                elif stack[-1] == q:
                    way_q = stack.copy()
            else:
                # поднимаемся и запоминаем что посетили
                visited.add(stack.pop())
                while stack[-1].right in visited:
                    visited.add(stack.pop())
                root = stack[-1]
        i = 0
        while i < min(len(way_p), len(way_q)):
            if way_p[i] != way_q[i]:
                break
            i += 1
        return way_q[i - 1]

    # ну удобно
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        # всё кроме нужного станет none
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

    # сравнимо с изначальным
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        # Строим словарь родителей пока не найдем оба узла
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # Находим предков p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        # Ищем первого общего предка с q
        while q not in ancestors:
            q = parent[q]
        return q



if __name__ == '__main__':
    node1 = TreeNode(7)
    node2 = TreeNode(4)
    node3 = TreeNode(0)
    node4 = TreeNode(2)
    node4.left = node1
    node4.right = node2
    node5 = TreeNode(6)
    node6 = TreeNode(5)
    node6.left = node5
    node6.right = node4
    inp = TreeNode(3, node6, TreeNode(1, node3, TreeNode(8)))
    print(Solution().lowestCommonAncestor(inp, node6, node3).val)

