from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # идея - рекурсивно разбивать массив листов пополам,
        # и как доходим до соседних listNode, начинать соединение
        # k: 16 -> 8 -> 4 -> 2 -> 1 - на последней итерации 1 финальный список
        if not lists:
            return None

        def merge_two(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def merge_lists(arr, left, right):
            if left == right:
                return arr[left]
            mid = (left + right) // 2
            l1 = merge_lists(arr, left, mid)
            l2 = merge_lists(arr, mid + 1, right)
            return merge_two(l1, l2)

        return merge_lists(lists, 0, len(lists) - 1)

if __name__ == '__main__':
    Solution().mergeKLists([
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(5))),
        ListNode(2, ListNode(6, ListNode(10)))
    ])
