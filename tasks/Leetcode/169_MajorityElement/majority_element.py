class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                major = nums[i]
            if nums[i] == major:
                count += 1
            else:
                count -= 1
        return major

    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2])