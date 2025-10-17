class Solution:
    def isHappy(self, n: int) -> bool:
        number_price = set()
        while n != 1:
            if n in number_price:
                return False
            number_price.add(n)
            s = 0
            while n > 0:
                last = n % 10
                s += last * last
                n //= 10
            n = s
        return True

    def isHappy1(self, n: int) -> bool:
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


if __name__ == '__main__':
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))