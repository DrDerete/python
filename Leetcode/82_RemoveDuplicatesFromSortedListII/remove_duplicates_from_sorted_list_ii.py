from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ans_head = ListNode(0, head)
        while head is not None:
            # последний уникальный элемент
            if head.next is None: break
            # скип копий / определение уникального
            uniq = True
            while head.next.val == head.val:
                head.next = head.next.next
                uniq = False
                if head.next is None: break
            if uniq:
                # перемещаемся на уникальный
                ans_head = head
            else:
                # забываем неуникальное
                ans_head.next = head.next
            head = head.next
        return ans.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return dummy.next


if __name__ == '__main__':
    inp3 = ListNode(1, ListNode(2, ListNode(2)))
    inp2 = ListNode(1, ListNode(1))
    inp1 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    Solution().deleteDuplicates(inp3)
    Solution().deleteDuplicates(inp2)
    Solution().deleteDuplicates(inp1)
