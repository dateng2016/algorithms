from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # R -> (n * 4 ** n)
        # S -> O(len(word) ** 2)   at a specific time point
        #                   the maximum length of the call stack is
        #                   len(word), the memory of all the
        #                   cur_string'S is 1 + 2 + ... + len(word) = O(len(word) ** 2)

        dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        r = len(board)
        c = len(board[0])

        ans = False

        def dfs(x, y, cur_string, nxt_ptr):
            nonlocal ans
            if nxt_ptr == len(word):
                ans = True
                return
            temp = board[x][y]
            board[x][y] = "*"
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if 0 <= xx < r and 0 <= yy < c and board[xx][yy] == word[nxt_ptr]:
                    dfs(xx, yy, cur_string + board[xx][yy], nxt_ptr + 1)
            board[x][y] = temp

        for i in range(r):
            for j in range(c):  # Assuming total number of elements is n, this is O(n)
                if ans:
                    return ans
                elif board[i][j] == word[0]:
                    dfs(i, j, board[i][j], 1)  # this is O(4 ** n)
        return ans

