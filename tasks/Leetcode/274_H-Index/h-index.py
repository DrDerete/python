class Solution(object):
    def hIndex1(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_i = []
        c = 0
        for value in sorted(citations):
            h_i.append(min(len(citations) - c, value))
            c += 1
        return max(h_i)

    def hIndex2(self, citations):
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)


if __name__ == '__main__':
    print(Solution().hIndex1([3, 0, 6, 1, 5]))
    print(Solution().hIndex1([1, 3, 1]))
    print(Solution().hIndex1([100]))
    print(Solution().hIndex1([0]))
    print(Solution().hIndex1([0, 3, 2, 0]))
