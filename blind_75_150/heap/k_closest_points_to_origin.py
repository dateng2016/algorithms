from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_distance(x, y):
            return (x**2 + y**2) ** 0.5

        for p in points:
            p.insert(0, cal_distance(p[0], p[1]))
        heapq.heapify(points)

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(points)
            res.append([x, y])
        return res


sol = Solution()
points = [[1, 3], [-2, 2]]
k = 1
res = sol.kClosest(points, k)

