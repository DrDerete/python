from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # идея - двигать указатель так, чтобы осталось не больше чем n + 1 node
        ans = head
        before_k, count = head, 0
        while head is not None:
            if count > n:
                before_k = before_k.next
            head = head.next
            count += 1
        if count > n:
            before_k.next = before_k.next.next
        else:
            ans = before_k.next
        return ans

    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # идея - сделать 2 указателя: в начале и на n + 1 node и двигать их
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

if __name__ == '__main__':
    inp1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().removeNthFromEnd(inp1, 2)
