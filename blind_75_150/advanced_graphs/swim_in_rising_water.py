from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # * NeetCode Guy

        # TODO:

        # * My Solution
        # * This problem requires you to find
        # * a route that has the MINIMUM MAXIMUM
        def get_nei_and_hei(x, y):
            # * Will append [point, height]
            res = []
            if 0 <= x - 1:
                res.append([(x - 1, y), grid[x - 1][y]])
            if 0 <= y - 1:
                res.append([(x, y - 1), grid[x][y - 1]])
            if x + 1 < n:
                res.append([(x + 1, y), grid[x + 1][y]])
            if y + 1 < n:
                res.append([(x, y + 1), grid[x][y + 1]])
            return res

        n = len(grid)
        if n == 1:
            return 0
        candidates = [(grid[0][0], (0, 0))]  # * (height, coordinate)
        visited = {(0, 0)}
        x, y = 0, 0
        ans = 0
        while True:
            height, (x, y) = heapq.heappop(candidates)
            ans = max(ans, height)
            visited.add((x, y))
            if x == n - 1 and y == n - 1:
                return ans
            print(f"Arr -> {get_nei_and_hei(x,y)}")
            for (xx, yy), height in get_nei_and_hei(x, y):
                if (xx, yy) in visited:
                    continue
                heapq.heappush(candidates, (height, (xx, yy)))
