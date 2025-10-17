from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # идея в том что head.random не получится указать для копии,
        # пока не существует её адрес. Поэтому сначала создаю копии всех node,
        # а потом заполняю их.
        if not head:
            return head
        head_begin = head
        association_nodes = {}
        new_nodes = []
        while head is not None:
            association_nodes[head] = len(new_nodes)
            node = Node(head.val)
            new_nodes.append(node)
            head = head.next
        head = head_begin
        deepcopy = deep_head = new_nodes[0]
        while head is not None:
            if head.next is not None:
               deep_head.next = new_nodes[association_nodes[head.next]]
            if head.random is not None:
                deep_head.random = new_nodes[association_nodes[head.random]]
            deep_head = deep_head.next
            head = head.next
        return deepcopy

    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # можно заполнять ссылку на следующий элемент при создании копий
        # и отдельно пройти по адресам старых узлов, заполняя node.random
        if not head:
            return head
        association_nodes = {head: 0}
        new_nodes = [Node(head.val)]

        while head.next is not None:
            association_nodes[head.next] = len(new_nodes)
            node = Node(head.next.val)
            new_nodes[-1].next = node
            new_nodes.append(node)
            head = head.next

        for node in association_nodes:
            if node.random is not None:
                new_nodes[association_nodes[node]].random = new_nodes[association_nodes[node.random]]

        return new_nodes[0]

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        indexes = [Node(head.val)]
        randoms = {head: 0}

        curr = head.next
        idx = 1

        while curr:
            randoms[curr] = idx

            new = Node(curr.val)
            indexes[-1].next = new
            indexes.append(new)

            curr = curr.next
            idx += 1

        for i, node in enumerate(randoms):
            if node.random in randoms:
                node.random = randoms[node.random]
                indexes[i].random = indexes[node.random]

        return indexes[0]

    def copyRandomList3(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # интересный подход, выйгрывает по памяти ... или нет, но во всяком случае интересный
        if not head:
            return None

        current = head

        # Step 1: Node interweaving
        # Original:  A -> B -> C
        # After Step 1: A -> A' -> B -> B' -> C -> C'
        while current:
            new = Node(current.val, current.next)
            current.next = new
            current = new.next

        current = head

        # Step 2: Assign random pointers
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate both lists
        original = head
        new_original = head.next
        copy_current = new_original
        while original:
            original.next = original.next.next
            if copy_current.next:
                copy_current.next = copy_current.next.next

            original = original.next
            copy_current = copy_current.next

        return new_original


if __name__ == '__main__':
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    Solution().copyRandomList1(node1)