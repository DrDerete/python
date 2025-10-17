from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev1, prev2 = 0, 0

        for num in nums:
            # Выбираем максимум между:
            # - ограблением текущего дома + предпоследний максимум
            # - пропуском текущего дома (предыдущий максимум)
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1