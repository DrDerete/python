class Solution(object):
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq_item = set()
        del_idx = []
        for i in range(len(nums)):
            if nums[i] not in uniq_item:
                uniq_item.add(nums[i])
            else:
                del_idx.append(i)
        for i in reversed(del_idx):
            del nums[i]
        return len(nums)

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            if nums[i] != nums[c]:
                c += 1
                nums[c] = nums[i]
        del nums[c + 1:]
        return c + 1


if __name__ == '__main__':
    Solution().removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
