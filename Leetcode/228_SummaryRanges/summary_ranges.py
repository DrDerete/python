from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums:
            return ans
        interval = []
        for n in nums:
            if len(interval) == 0:
                interval = [n, None]
            else:
                if interval[1] is None:
                    if n == interval[0] + 1:
                        interval[1] = n
                    else:
                        ans.append(str(interval[0]))
                        interval[0] = n
                else:
                    if n == interval[1] + 1:
                        interval[1] = n
                    else:
                        ans.append("->".join(map(str, interval)))
                        interval = [n, None]
        if interval[1] is None:
            ans.append(str(interval[0]))
        else:
            ans.append("->".join(map(str, interval)))
        return ans

    def summaryRanges1(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        left = 0
        while left < n:
            right = left
            while right + 1 < n and nums[right] + 1 == nums[right + 1]:
                right += 1
            if left == right:
                res.append(str(nums[left]))
            else:
                res.append(f"{nums[left]}->{nums[right]}")
            left = right + 1
        return res


if __name__ == '__main__':
    print(Solution().summaryRanges([0,1,2,4,5,7]))