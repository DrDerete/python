from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(intervals) < 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        inter = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= inter[1]:
                if intervals[i][1] >= inter[1]:
                    inter[1] = intervals[i][1]
            else:
                ans.append(inter)
                inter = [intervals[i][0], intervals[i][1]]
        ans.append(inter)
        return ans

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        # тратим меньше памяти - сортировка изначального массива и убиваем inter
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged

if __name__ == '__main__':
    print(Solution().merge([[1,4],[2,3],[0,10]]))
    print(Solution().merge([[1,4],[0,4]]))
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
    print(Solution().merge([[1,4],[4,5]]))
    print(Solution().merge([[4,7],[1,4]]))