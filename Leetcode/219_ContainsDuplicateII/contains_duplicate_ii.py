from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_idx = {}
        for i in range(len(nums)):
            if nums[i] in num_to_idx:
                if i - num_to_idx[nums[i]] <= k:
                    return True
            num_to_idx[nums[i]] = i
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
    print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
    print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
