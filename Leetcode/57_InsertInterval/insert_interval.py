from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        if not intervals:
            ans.append(newInterval)
            return ans
        if not newInterval:
            return intervals
        begin = 0
        while newInterval[0] > intervals[begin][1]:
            ans.append(intervals[begin])
            begin += 1
            if begin > len(intervals) - 1:
                ans.append(newInterval)
                return ans
        end = begin
        while newInterval[1] > intervals[end][1]:
            end += 1
            if end > len(intervals) - 1:
                ans.append([min(intervals[begin][0], newInterval[0]), newInterval[1]])
                return ans
        if end == begin:
            if intervals[end][0] > newInterval[1]:
                ans.append(newInterval)
            else:
                ans.append([min(intervals[end][0], newInterval[0]), intervals[end][1]])
                end += 1
        else:
            if intervals[end][0] > newInterval[1]:
                ans.append([min(intervals[begin][0], newInterval[0]), newInterval[1]])
            else:
                ans.append([min(intervals[begin][0], newInterval[0]), intervals[end][1]])
                end += 1
        while end != len(intervals):
            ans.append(intervals[end])
            end += 1
        return ans

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # сразу переписываем границы нового интервала, что
        # позволяет избавится от выносящей мозг логики
        if not newInterval:
            return intervals

        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result



if __name__ == '__main__':
    print(Solution().insert1([[1,3],[6,9]], [2, 5]))
    print(Solution().insert1([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
    print(Solution().insert1([[1,5]], [2, 3]))
