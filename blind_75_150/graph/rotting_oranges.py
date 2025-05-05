from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        R -> O(r * c)
        S -> O(1)
        """
        time = -1
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not q:
            # * This mean that there is no rotted oranges
            for row in grid:
                for status in row:
                    if status == 1:
                        return -1
            return 0
        while q:
            l = len(q)
            for _ in range(l):
                i, j = q.popleft()
                for di, dj in dirs:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        q.append((ii, jj))
            time += 1
        for row in grid:
            for status in row:
                if status == 1:
                    return -1
        return time

