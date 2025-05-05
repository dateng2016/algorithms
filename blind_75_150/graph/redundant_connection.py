from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        found_cycle = False
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i, destination, before, visited):
            nonlocal found_cycle
            visited.add(i)
            if found_cycle:
                return
            for nei in graph[i]:
                if nei == before:
                    continue
                elif nei == destination:
                    found_cycle = True
                    return
                elif nei in visited:
                    return
                else:
                    dfs(nei, destination, i, visited)
                    if found_cycle:
                        return

        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i]
            if a not in visited:
                dfs(a, b, b, set())
                if found_cycle:
                    return [a, b]


s = Solution()
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
res = s.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
print(res)

