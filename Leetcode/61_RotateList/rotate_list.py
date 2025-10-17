from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        rotate = head
        length = 1
        while rotate.next is not None:
            length += 1
            rotate = rotate.next
        rotate.next = head
        end_point = k % length
        while length != end_point:
            rotate = rotate.next
            length -= 1
        head = rotate.next
        rotate.next = None
        return head

if __name__ == '__main__':
    inp1 = ListNode(1, ListNode(2, ListNode(3)))
    inp2 = ListNode(1, ListNode(2, ListNode(3)))
    Solution().rotateRight(inp1, 2)
    Solution().rotateRight(inp2, 4)
