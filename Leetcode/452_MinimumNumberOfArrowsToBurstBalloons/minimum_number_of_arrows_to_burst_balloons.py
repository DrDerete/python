from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])
        inter = points[0]
        count_arrows = 0
        i = 1
        while i < len(points):
            if inter[1] < points[i][0]:
                count_arrows += 1
                inter = points[i]
            else:
                inter = [max(inter[0], points[i][0]), min(inter[1], points[i][1])]
            i += 1
        return count_arrows + 1

    def findMinArrowShots1(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end_border = points[0][1]
        count_arrows = 0
        for p in points:
            if p[0] > end_border:
                count_arrows += 1
                end_border = p[1]
        return count_arrows + 1



if __name__ == '__main__':
    print(Solution().findMinArrowShots1([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
    print(Solution().findMinArrowShots1([[10,16],[2,8],[1,6],[7,12]]))
    print(Solution().findMinArrowShots1([[1,2],[3,4],[5,6],[7,8]]))
    print(Solution().findMinArrowShots1([[1,2],[2,3],[3,4],[4,5]]))