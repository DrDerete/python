from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = head = ListNode()
        residual = 0
        while l1 is not None or l2 is not None or residual:
            number = 0
            if l1 is not None:
                number += l1.val
                l1 = l1.next
            if l2 is not None:
                number += l2.val
                l2 = l2.next
            number += residual
            # Создаем вершину и добавляем
            node = ListNode(number % 10)
            residual = number // 10
            head.next = node
            head = node
        return ans.next


if __name__ == '__main__':
    inp1 = ListNode(2, ListNode(4, ListNode(3, None)))
    inp2 = ListNode(5, ListNode(6, ListNode(4, None)))
    Solution().addTwoNumbers(inp1, inp2)
    inp1 = ListNode(0)
    inp2 = ListNode(0)
    Solution().addTwoNumbers(inp1, inp2)