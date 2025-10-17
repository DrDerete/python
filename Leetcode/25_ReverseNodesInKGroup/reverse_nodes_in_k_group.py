from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # после прошлых задач на списки даже быстро
        if k < 2:
            return head
        ans_list = ans_head = ListNode()
        while head is not None:
            end = None
            end_node = None
            k_reverse = None
            # переворачиваем k элементов
            for _ in range(k):
                if head is None: break
                if end_node is None: end_node = head
                next_node = head.next
                head.next = k_reverse
                k_reverse = head
                head = next_node
            else:
                # если переворот завершился соединяем списки
                ans_head.next = k_reverse
                ans_head = end_node
                end = True
            # а если нет, то это конец,
            # но надо еще раз перевернуть перевернутое
            if end is None:
                end_reverse = None
                while k_reverse is not None:
                    next_node = k_reverse.next
                    k_reverse.next = end_reverse
                    end_reverse = k_reverse
                    k_reverse = next_node
                ans_head.next = end_reverse
        return ans_list.next

class Solution1:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


if __name__ == '__main__':
    Solution().reverseKGroup(ListNode(1, ListNode(2)), 2)
    Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)