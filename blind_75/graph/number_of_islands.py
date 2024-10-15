from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # R -> O(n) because each element cannot be went through more than twice
        # S -> O(n) account for the call stack

        r = len(grid)
        c = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(x, y):
            grid[x][y] = "*"
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if 0 <= xx < r and 0 <= yy < c and grid[xx][yy] == "1":
                    dfs(xx, yy)

        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans

