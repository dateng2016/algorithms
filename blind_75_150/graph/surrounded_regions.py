from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        edge_coord = []
        rows = len(board)
        cols = len(board[0])
        should_not_change = set()
        for i in range(rows):
            if board[i][0] == "O":
                edge_coord.append((i, 0))
            if board[i][cols - 1] == "O":
                edge_coord.append((i, cols - 1))
        for j in range(cols):
            if board[0][j] == "O":
                edge_coord.append((0, j))
            if board[rows - 1][j] == "O":
                edge_coord.append((rows - 1, j))

        def dfs(x, y):
            should_not_change.add((x, y))
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if (
                    0 <= xx < rows
                    and 0 <= yy < cols
                    and board[xx][yy] == "O"
                    and (xx, yy) not in should_not_change
                ):
                    dfs(xx, yy)

        print(edge_coord)
        for i, j in edge_coord:
            dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in should_not_change:
                    board[i][j] = "X"

