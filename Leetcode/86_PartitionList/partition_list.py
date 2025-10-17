from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smoller_nodes = sm_head = ListNode()
        higher_nodes = h_head = ListNode()
        while head is not None:
            if head.val < x:
                sm_head.next = head
                sm_head = sm_head.next
            else:
                h_head.next = head
                h_head = h_head.next
            head = head.next
        h_head.next = None
        sm_head.next = higher_nodes.next
        return smoller_nodes.next


if __name__ == '__main__':
    inp = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    Solution().partition(inp, 3)