from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)

            return node

        return build_tree(0, len(nums) - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == '__main__':
    Solution().sortedArrayToBST([-10, -3, 0, 5, 9])


