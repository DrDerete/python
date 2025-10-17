from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Если можем взять все проекты, просто берем k самых прибыльных
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Добавляем все доступные проекты
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w