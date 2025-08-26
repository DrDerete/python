class Solution(object):
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return 0
        c = 0  # количество прыжков
        i = 0  # клетка положения
        fuel = nums[i]
        while fuel < len(nums) - 1 - i:
            c += 1
            max_f = None  # крутая клетка
            for j in range(i + 1, i + 1 + fuel):
                if max_f is None:
                    if nums[j] != 0:
                        max_f = j
                elif nums[j] > nums[max_f] - (j - max_f):
                    max_f = j
            if max_f is None:
                return "мы в беде"
            fuel = nums[max_f]
            i = max_f
        return c + 1

    def canJump2(self, nums):
        # для решения задачи подходит, но не обрабатывается проигрыш
        l, r, ans = 0, 0, 0
        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(i + nums[i], far)
                # гуд идея -------------------------------------------------
                # при каждом прыжке бак обнуляется, поэтому необходимо найти
                # в какой клетке добираемся до финиша
            l = r + 1
            r = far
            ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().canJump2([3, 0, 0, 0]))
    print(Solution().canJump2([3, 4, 3, 2, 5, 4, 3]))
    print(Solution().canJump2([3, 4, 3, 3, 5, 4, 3]))
