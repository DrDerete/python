from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        curse_load = [0] * numCourses
        curse_order = {}
        for curse, requirement in prerequisites:
            curse_load[curse] += 1
            if requirement not in curse_order:
                curse_order[requirement] = []
            curse_order[requirement].append(curse)

        free_curses = []
        for cur, loaded in enumerate(curse_load):
            if loaded == 0:
                free_curses.append(cur)

        ans = []
        while free_curses:
            cur = free_curses.pop()
            ans.append(cur)
            if cur in curse_order:
                next_curs = curse_order.pop(cur)
                for c in next_curs:
                    curse_load[c] -= 1
                    if curse_load[c] == 0:
                        free_curses.append(c)
        return ans if sum(curse_load) == 0 else []

    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        N = numCourses
        graph = defaultdict(list)
        indeg = [0] * N

        for v, u in prerequisites:
            graph[u].append(v)
            indeg[v] += 1

        que = deque([i for i in range(N) if indeg[i] == 0])
        res = []
        while que:
            u = que.popleft()
            res.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    que.append(v)

        return res if len(res) == N else []

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited, cycle = set(), set()
        result = []

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            result.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result

if __name__ == '__main__':
    Solution().findOrder(2, [[1,0]])
    Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
