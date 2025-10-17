from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 1

        for i in range(len(points)):
            slope_count = {}
            duplicate = 0
            current_max = 0

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Проверяем совпадающие точки
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue

                # Вычисляем наклон с нормализацией
                dx = x2 - x1
                dy = y2 - y1

                # Находим НОД для нормализации
                g = gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g

                # Убеждаемся в единообразии знака
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0 and dy < 0:
                    dy = -dy

                slope = (dx, dy)
                slope_count[slope] = slope_count.get(slope, 0) + 1
                current_max = max(current_max, slope_count[slope])

            max_points = max(max_points, current_max + duplicate + 1)

        return max_points