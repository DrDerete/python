class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Сдвигаем результат влево и добавляем младший бит n
            result = (result << 1) | (n & 1)
            # Сдвигаем n вправо для получения следующего бита
            n >>= 1
        return result