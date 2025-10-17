class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:  # если n нечетное
                result *= x
            x *= x  # возводим x в квадрат
            n //= 2  # уменьшаем n вдвое

        return result