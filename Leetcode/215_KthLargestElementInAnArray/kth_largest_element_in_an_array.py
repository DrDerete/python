import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap размера k
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)  # Удаляем наименьший элемент

        return heap[0]  # k-й наибольший элемент - корень кучи