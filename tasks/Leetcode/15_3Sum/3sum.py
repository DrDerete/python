from collections import Counter
from bisect import bisect_left, bisect_right


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # мне это нравится, гуд по всему 90%+
        ans = set()
        nums.sort()

        i, j, k = 0, 1, len(nums) - 1

        if nums[k] < 0 or nums[i] > 0:
            return list(ans)

        if nums[k] == 0 and k > 1:
            if nums[k] == nums[k - 2]:
                ans.add((0, 0, 0))
            return list(ans)

        while nums[i] <= 0:
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
            while nums[i] == nums[i + 1]:
                i += 1
            i += 1
            k = len(nums) - 1
            j = i + 1
        return list(ans)

    def threeSum1(self, nums):
        # избегание повторов через while, показывает себя хуже
        ans = []
        nums.sort()

        i, j, k = 0, 1, len(nums) - 1

        if nums[k] < 0 or nums[i] > 0:
            return list(ans)

        if nums[k] == 0 and k > 1:
            if nums[k] == nums[k - 2]:
                ans.append([0, 0, 0])
            return ans

        while nums[i] <= 0:
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            while nums[i] == nums[i + 1]:
                i += 1
            i += 1
            k = len(nums) - 1
            j = i + 1
        return ans

    def threeSum2(self, nums):
        # самый быстрый, но по памяти 20%
        count = Counter(nums)
        sorted_set = sorted(count)
        ans = []

        for i, num in enumerate(sorted_set):
            if count[num] > 1:
                if num == 0:
                    if count[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -2 * num in count:
                        ans.append([num, num, -2 * num])
            if num < 0:
                sum2 = -num
                left = bisect_left(sorted_set, (sum2 - sorted_set[-1]), i + 1)
                right = bisect_right(sorted_set, (sum2 // 2), left)
                for i in sorted_set[left:right]:
                    j = sum2 - i
                    if j in count and j != i:
                        ans.append([num, i, j])
        return ans

    def threeSum3(self, nums):
        # лаконичный, но самый средний
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum1([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum1([1, 1, 1]))
    print(Solution().threeSum1([-2, -3, 0, 0, -2]))
    print(Solution().threeSum1([0, 0, 0]))
    print(Solution().threeSum1([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]))
    print(Solution().threeSum1([5, -1, 0, 1, 3, 2, -7, 0, -1, 1, 3, 2, -2, 4, -1, -4]))
    print(Solution().threeSum1([-1, 0, 1, 2, -1, -4]))
