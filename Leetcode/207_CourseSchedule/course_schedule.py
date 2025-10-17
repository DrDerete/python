from collections import deque
from typing import List

class Solution:
    # по сути необходимо очередность курсов на противоречие
    # !только когда решил что задача зеркально и надо first и second поменять местами!
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # поскольку курсы нумеруются по порядку,
        # используем массив для отображения загруженности (курс можно проходить когда загруженности у него нет)
        # а порядок правил сохраним в мапу - таким образом мы будем знать нагруженность с какого курса понизим
        curse_load = [0] * numCourses
        curse_order = {}
        for first, second in prerequisites:
            curse_load[second] += 1
            if first not in curse_order:
                curse_order[first] = []
            curse_order[first].append(second)
        # функция снижения нагрузки с курсов
        def trust_order(order, load, cur):
            load[cur] = -1
            if cur not in order:
                return
            next_cur = order.pop(cur)
            for c in next_cur:
                load[c] -= 1
                if load[c] == 0:
                    trust_order(order, load, c)
        # проходим ко курсам без нагруженности и снимаем её с остальных
        for i in range(len(curse_load)):
            if curse_load[i] == 0:
                trust_order(curse_order, curse_load, i)
        # если правила остались, то где-то перегрузка
        return len(curse_order) == 0

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        preqCourse = [[] for i in range(numCourses)]
        courseVisited = 0

        for a, b in prerequisites:
            indegree[a] += 1
            preqCourse[b].append(a)

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            courseVisited += 1

            for nei in preqCourse[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return courseVisited == numCourses

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        def has_cycle(state):
            if visited[state] == 1:
                return True
            if visited[state] == 2:
                return False
            visited[state] = 1
            for neighbor in graph[state]:
                if has_cycle(neighbor):
                    return True
            visited[state] = 2
            return False

        visited = [0] * numCourses
        for course in range(numCourses):
            if visited[course] == 0 and has_cycle(course):
                return False
        return True

if __name__ == '__main__':
    print(Solution().canFinish2(5, [[1,4],[2,4],[3,1],[3,2]]))
    print(Solution().canFinish2(3, [[2,1],[1,0]]))
    print(Solution().canFinish(2, [[1,0]]))
    print(Solution().canFinish(2, [[1,0], [0, 1]]))

