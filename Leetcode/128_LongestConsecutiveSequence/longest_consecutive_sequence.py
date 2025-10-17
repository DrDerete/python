from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # со скрипом пройдено
        if not nums:
            return 0

        nums = set(nums)
        min_to_l = {}
        while len(nums):
            # отсекаем вершины, которые влазят в len(nums)
            min_n = min(nums)
            del_set = set()
            for ch in nums:
                if ch - min_n - len(nums) < 0:
                    del_set.add(ch)

            # считаем полученные в них последовательности
            l, c = 0, 0
            num = min_n
            for i in range(len(del_set)):
                if min_n + i + c not in del_set:
                    min_to_l[num] = l
                    while min_n + i + c not in del_set:
                        c += 1
                    num = min_n + i + c
                    l = 1
                else:
                    l += 1
            min_to_l[num] = l
            # переписываем без посчитанных
            nums = {ch for ch in nums if ch not in del_set}

        # костыль на объединение последовательностей
        for key in min_to_l:
            if key + min_to_l[key] in min_to_l:
                min_to_l[key] += min_to_l[key + min_to_l[key]]

        # последовательность максимальной длины
        return max(min_to_l.values())


    def longestConsecutive1(self, nums: List[int]) -> int:
        # а вот так по-человечески, просто проверка является ли число началом
        # и сразу хочется жить ...
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

if __name__ == '__main__':
    print(Solution().longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
    print(Solution().longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))
    print(Solution().longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(Solution().longestConsecutive([0,0]))
    print(Solution().longestConsecutive([0,-1]))
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
    print(Solution().longestConsecutive([1,0,1,2]))
