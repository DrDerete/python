class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Находим общий префикс left и right
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        # Сдвигаем обратно на найденное количество битов
        return left << shift