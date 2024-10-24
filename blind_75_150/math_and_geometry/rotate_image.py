from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                top_left = matrix[top][l + i]

                # We move the bottom LEFT to TOP left
                matrix[top][l + i] = matrix[bottom - i][l]

                # We move the BOTTOM right to bottom LEFT
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # We move the top RIGHT to BOTTOM right
                matrix[bottom][r - i] = matrix[top + i][r]

                # FINALLY, we move the TOP left to top RIGHT
                matrix[top + i][r] = top_left
            l += 1
            r -= 1

