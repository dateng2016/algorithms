from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We use a reference list to keep track whether it can reach
        # Pacific and Atalantic Ocean

        # R -> O(n) In the worst case, the entire island has the same heights
        #       Each element can be went through no more than twice
        # S -> O(n) to keep the two tracker lists

        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        r = len(heights)
        c = len(heights[0])
        pacific = [[0 for _ in range(c)] for _ in range(r)]
        atlantic = [[0 for _ in range(c)] for _ in range(r)]

        def reach_pacific(x, y):
            pacific[x][y] = 1
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if (
                    0 <= xx < r
                    and 0 <= yy < c
                    and pacific[xx][yy] == 0
                    and heights[xx][yy] >= heights[x][y]
                ):
                    reach_pacific(xx, yy)

        def reach_atlantic(x, y):
            # print(x, y)
            atlantic[x][y] = 1
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if (
                    0 <= xx < r
                    and 0 <= yy < c
                    and atlantic[xx][yy] == 0
                    and heights[xx][yy] >= heights[x][y]
                ):
                    reach_atlantic(xx, yy)

        for j in range(c):
            if pacific[0][j] == 0:
                reach_pacific(0, j)
            if atlantic[r - 1][j] == 0:
                reach_atlantic(r - 1, j)

        for i in range(r):
            if pacific[i][0] == 0:
                reach_pacific(i, 0)
            if atlantic[i][c - 1] == 0:
                reach_atlantic(i, c - 1)
        res = []
        for i in range(r):
            for j in range(c):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i, j])
        return res

