from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # мерзость
        reverse_list = head
        idx = 1
        adr_to_reverse = []
        while head is not None:
            if idx >= left - 1:
                undo_reverse = None if left == 1 else head
                if undo_reverse:
                    head = head.next
                for i in range(right - left + 1):
                    adr_to_reverse.append(head)
                    head = head.next
                after_reverse = None if head is None else head

                revers = ListNode() if undo_reverse is None else undo_reverse
                revers_head = revers
                for i in range(len(adr_to_reverse) - 1, -1, -1):
                    revers_head.next = adr_to_reverse[i]
                    revers_head = adr_to_reverse[i]
                revers_head.next = after_reverse

                if undo_reverse is None:
                    reverse_list = revers.next
                break
            else:
                head = head.next
            idx += 1
        return reverse_list

    def reverseBetween1(self, head, left, right):
        # культура
        reverse_list = before_rev = ListNode(0)
        reverse_list.next = head
        for _ in range(left - 1):
            before_rev = before_rev.next

        node = before_rev.next
        reversed_nodes = None

        for _ in range(right - left + 1):
            next_node = node.next
            node.next = reversed_nodes
            reversed_nodes = node
            node = next_node

        before_rev.next.next = node
        before_rev.next = reversed_nodes
        return reverse_list.next

if __name__ == '__main__':
    inp1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    inp2 = ListNode(3, ListNode(5))
    Solution().reverseBetween1(inp1, 2, 4)
    Solution().reverseBetween1(inp2, 1, 2)
