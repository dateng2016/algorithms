from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # R -> O(m * n)
        # S -> O(m * n)
        rows = set()
        cols = set()

        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(c):
                matrix[i][j] = 0
        for i in range(r):
            for j in cols:
                matrix[i][j] = 0


s = "Set Matrix Zeroes.py".lower()
ls = s.split(" ")
print("_".join(ls))

