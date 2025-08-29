class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        del_list = []
        for i in range(len(nums)):
            if nums[i] == val:
                del_list.append(i)
        for idx in reversed(del_list):
            del nums[idx]
        return len(nums)


if __name__ == '__main__':
    Solution().removeElement([3, 2, 2, 3], 3)
    Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
