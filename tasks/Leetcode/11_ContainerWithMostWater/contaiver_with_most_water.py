class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(height) - 1
        water_max = 0
        while p1 < p2:
            water = (p2 - p1) * min(height[p1], height[p2])
            water_max = water if water > water_max else water_max
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return water_max

    def maxArea1(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        max_height = max(height)

        while left < right:
            if max_area >= (right - left) * max_height: break

            w = right - left
            h = height[left] if height[left] <= height[right] else height[right]

            max_area = max_area if max_area >= h * w else h * w

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([1, 1]))
