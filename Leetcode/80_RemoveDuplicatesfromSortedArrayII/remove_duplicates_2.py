class Solution(object):
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq_count = {}
        del_idx = []
        for i in range(len(nums)):
            if nums[i] not in uniq_count:
                uniq_count[nums[i]] = 1
            elif uniq_count[nums[i]] == 1:
                uniq_count[nums[i]] += 1
            else:
                del_idx.append(i)
        for i in reversed(del_idx):
            del nums[i]
        return len(nums)

    def removeDuplicates2(self, nums):
        if not nums:
            return 0
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    Solution().removeDuplicates2([1, 1, 1, 2, 2, 3])
