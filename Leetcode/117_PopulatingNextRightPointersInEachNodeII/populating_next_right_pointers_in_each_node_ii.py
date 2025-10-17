class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        new_stack = []
        while stack:
            for n in stack:
                if n.left:
                    new_stack.append(n.left)
                if n.right:
                    new_stack.append(n.right)
            for i in range(len(new_stack) - 1):
                new_stack[i].next = new_stack[i + 1]
            stack = new_stack
            new_stack = []
        return root

    def connect1(self, root):
        if not root:
            return root
        level = [root]
        while level:
            next_level = []
            for i in range(len(level)):
                node = level[i]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if i < len(level) - 1:
                    node.next = level[i + 1]
            level = next_level
        return root

    def connect2(self, root):
        if not root:
            return root
        head = root
        while head:
            dummy = Node(0)
            current = dummy
            while head:
                if head.left:
                    current.next = head.left
                    current = current.next
                if head.right:
                    current.next = head.right
                    current = current.next
                head = head.next
            head = dummy.next
        return root


if __name__ == '__main__':
    Solution().connect(Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7))))
