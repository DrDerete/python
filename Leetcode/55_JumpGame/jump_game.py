class Solution(object):
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fuel = nums[0]
        for n in nums[1:]:
            fuel -= 1
            if fuel < 0:
                return False
            elif n > fuel:
                fuel = n
        return True

    def canJump2(self, nums):
        # чуть меньше памяти, но медленнее, если верить leetcode
        max_dest = 0
        i = 0
        while i <= max_dest:
            if max_dest >= len(nums) - 1:
                return True

            elif i + nums[i] > max_dest:
                max_dest = i + nums[i]
            i += 1

        return False


if __name__ == '__main__':
    print(Solution().canJump2([0, 1]))
