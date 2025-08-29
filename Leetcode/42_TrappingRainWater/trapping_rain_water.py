class Solution(object):
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # так получилось медленно, если pit становится большим, то траблы
        water = 0  # сколько воды накАпало
        pit = {}  # {глубины: длинна}
        wall = 0  # начало ямы
        for h in height:
            if wall == 0:
                if h > 0:
                    wall = h
            else:
                if h < wall:  # если это не конец ямы
                    deep = wall - h  # смотрим какая глубина
                    keys = [key for key in pit.keys() if key >= wall - h]  # какая глубина уже точно наполнится
                    if not keys:  # если яма пока пуста
                        pit[deep] = 1
                    else:  # наполняем что можем
                        for key in keys:
                            pit_l = pit.pop(key)
                            pit_h = key - deep
                            water += pit_l * pit_h
                            if deep in pit:
                                pit[deep] += pit_l
                            else:
                                pit[deep] = pit_l
                        pit[deep] += 1
                else:  # если яма кончилась, она полностью наполняется
                    water += sum(key * pit[key] for key in pit)
                    pit.clear()
                    wall = h
        pit.clear()
        return water

    def trap(self, height):
        # 92% 80%
        # Движемся с двух сторон и всегда с той, где меньше высота - это гарантирует
        # что вода будет оставаться и не утекать, а значит её сразу можно добавлять.
        water = 0
        left, right = 0, len(height) - 1
        max_l, max_r = height[left], height[right]
        while left < right:
            if max_l > max_r:
                right -= 1
                if height[right] > max_r:
                    max_r = height[right]
                else:
                    water += max_r - height[right]
            else:
                left += 1
                if height[left] > max_l:
                    max_l = height[left]
                else:
                    water += max_l - height[left]
        return water


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(Solution().trap([4, 2, 0, 3, 2, 5]))  # 9
    print(Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))  # 23
