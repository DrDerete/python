from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # используем dict для быстрого поиска остатка от target
        remains = {}
        for i in range(len(nums)):
            if target - nums[i] in remains:
                return [remains[target - nums[i]], i]
            remains[nums[i]] = i
        return None

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # полный перебор
        output = []
        for i in range(len(nums)):
            temp1 = nums[i]
            for j in range(i+1, len(nums)):
                temp2 = nums[j]
                if temp1 + temp2 == target:
                    output = [i, j]
        return output



if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))