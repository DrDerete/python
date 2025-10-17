from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        values.sort()

        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # если вершина последняя, возвращаемся
        if not head or not head.next:
            return head
        # в противном случае доходим до середины списка
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # и продолжаем разбиение полученных подсписков
        right = self.sortList1(slow.next)
        slow.next = None
        left = self.sortList1(head)
        # когда дошли до конца разбиения, начинается слияние
        dummy = curr = ListNode(0)
        while left and right:
            if left.val < right.val:
                curr.next, left = left, left.next
            else:
                curr.next, right = right, right.next
            curr = curr.next
        curr.next = left or right
        # возвращаем отсортированный список
        return dummy.next

if __name__ == '__main__':
    Solution().sortList1(ListNode(4, ListNode(2, ListNode(3, ListNode(-2, ListNode(10))))))
