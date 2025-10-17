from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  # биты, появившиеся один раз
        twos = 0  # биты, появившиеся два раза

        for num in nums:
            # Обновляем ones: добавляем новые биты и убираем те, что уже в twos
            ones = (ones ^ num) & ~twos
            # Обновляем twos: добавляем биты из ones и убираем обработанные
            twos = (twos ^ num) & ~ones

        return ones