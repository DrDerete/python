class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            nums1[:] = nums2
            return

        if not n:
            return

        s = n + m - 1
        while s >= 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[s] = nums1[m - 1]
                m -= 1
                if not m:
                    nums1[:s] = nums2[:n]
                    break
            else:
                nums1[s] = nums2[n - 1]
                n -= 1
                if not n:
                    break
            s -= 1

    # ага, а теперь читать условие
    def split_sort(self, arr):
        sort = []

        if len(arr) == 1:
            return arr

        middle = len(arr) // 2
        first = self.split_sort(arr[:middle])
        second = self.split_sort(arr[middle:])

        while True:
            if first[-1] > second[-1]:
                sort.append(first.pop())
            else:
                sort.append(second.pop())
            if len(first) == 0:
                sort.extend(reversed(second))
                break
            if len(second) == 0:
                sort.extend(reversed(first))
                break
        return list(reversed(sort))


if __name__ == '__main__':
    # m отсортированных элементов из 122_BestTimeToBuy2 аrr и n из 2 аrr
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    Solution().merge([2, 0], 1, [1], 1)
    Solution().merge([1], 1, [], 0)
    Solution().merge([0], 0, [1], 1)
