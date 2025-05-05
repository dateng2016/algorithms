from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        R -> O(r * c)
        S -> O(1)
        """
        ans = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            grid[x][y] = "*"
            nonlocal ans
            area = 1
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                    area += dfs(xx, yy)
            ans = max(ans, area)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
        return ans

