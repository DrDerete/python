class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # выигрыш в памяти
        p1, p2 = 0, len(numbers) - 1
        while numbers[p1] + numbers[p2] != target:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1
        return [p1 + 1, p2 + 1]

    def twoSum1(self, numbers, target):
        # выйгрыш в скорости
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1


if __name__ == '__main__':
    print(Solution().twoSum1([-1, 0], -1))
    print(Solution().twoSum1([2, 7, 11, 15], 9))
    print(Solution().twoSum1([2, 3, 4], 6))
    print(Solution().twoSum1([-3, 3, 4, 90], 0))
