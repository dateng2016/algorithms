from typing import List
import heapq
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # * Prim's Algorithm
        # * n points -> (n - 1) edges without creating a cycle

        # * Time complexity -> O(n ** 2 log(n))
        # * Space complexity -> O(n ** 2)
        def calc_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        graph = defaultdict(list)
        for i in range(len(points)):
            point1 = points[i]
            for j in range(i + 1, len(points)):
                point2 = points[j]
                graph[i].append((calc_dist(p1=point1, p2=point2), j))
                graph[j].append((calc_dist(p1=point1, p2=point2), i))

        total_cost = 0
        visited = set()
        min_heap = [[0, 0]]  # * [distance, point_idx]
        while len(visited) < len(points):
            cost, next_point_idx = heapq.heappop(min_heap)
            if next_point_idx in visited:
                continue
            total_cost += cost
            for nei_cost, nei in graph[next_point_idx]:
                heapq.heappush(min_heap, [nei_cost, nei])

            visited.add(next_point_idx)
        return total_cost
