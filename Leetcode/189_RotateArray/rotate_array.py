class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


if __name__ == '__main__':
    Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)