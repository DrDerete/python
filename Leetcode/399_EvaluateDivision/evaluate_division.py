from collections import deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # типо {a: {b: 2.0}, b: {a: 0.5, c: 3.0} c: {b: 0.33}}
        mem = {}
        for (ch1, ch2), val in zip(equations, values):
            if ch1 not in mem:
                mem[ch1] = {}
            if ch2 not in mem:
                mem[ch2] = {}
            mem[ch1][ch2] = val
            mem[ch2][ch1] = 1 / val
        # вычисление уравнений
        ans = []
        def count_prod(start, target, vis, current):
            if start == target:
                return current
            vis.add(start)
            for neighbour, weight in mem[start].items():
                if neighbour not in vis:
                    result = count_prod(neighbour, target, vis, current * weight)
                    if result != -1.0:
                        return result
            return -1.0
        for q in queries:
            if q[0] not in mem or q[1] not in mem:
                ans.append(-1.0)
            else:
                visited = set()
                ans.append(count_prod(q[0], q[1], visited, 1.0))
        return ans

    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build graph
        graph = {}
        for (a, b), val in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        results = []

        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
                continue

            if a == b:
                results.append(1.0)
                continue

            # BFS search
            queue = deque()
            queue.append((a, 1.0))
            visited = {a}
            found = False

            while queue and not found:
                node, product = queue.popleft()

                for neighbor, weight in graph[node].items():
                    if neighbor == b:
                        results.append(product * weight)
                        found = True
                        break
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * weight))

            if not found:
                results.append(-1.0)

        return results

    # вау
    def calcEquation2(self, equations, values, queries):
        graph = {}
        for (a, b), v in zip(equations, values):
            graph.setdefault(a, {})[b] = v
            graph.setdefault(b, {})[a] = 1 / v

        def dfs(a, b, visited):
            if a == b: return 1.0
            visited.add(a)
            for n, w in graph.get(a, {}).items():
                if n not in visited:
                    res = dfs(n, b, visited)
                    if res != -1: return w * res
            return -1.0

        return [dfs(a, b, set()) if a in graph and b in graph else -1.0 for a, b in queries]



if __name__ == '__main__':
    Solution().calcEquation(
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    )
