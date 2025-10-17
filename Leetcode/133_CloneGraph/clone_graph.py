from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # {node: new_node}
        if not node:
            return None
        cloned = {}
        queue = deque([node])
        cloned[node] = Node(node.val)
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]

    def cloneGraph1(self, node: Optional['Node']) -> Optional['Node']:
        # красивое
        cloned = {}
        def dfs(node):
            if node in cloned:
                return cloned[node]
            copy = Node(node.val)
            cloned[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node) if node else None


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    Solution().cloneGraph(n1)
