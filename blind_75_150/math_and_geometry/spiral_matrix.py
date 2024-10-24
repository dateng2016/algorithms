from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        This traverse the whole thing
        R -> O(n ** 2)
        S -> O(n ** 2)
        """

        res = []
        seen = set()
        i = j = -1
        go_right = True
        go_down = False
        go_left = False
        go_up = False

        r, c = len(matrix), len(matrix[0])

        while len(res) < r * c:
            if go_right:
                i += 1
                j += 1
                while j < c and (i, j) not in seen:
                    res.append(matrix[i][j])
                    seen.add((i, j))
                    j += 1
                go_right = False
                go_down = True
            elif go_down:
                j -= 1
                i += 1
                while i < r and (i, j) not in seen:
                    res.append(matrix[i][j])
                    seen.add((i, j))
                    i += 1
                go_down = False
                go_left = True
            elif go_left:
                j -= 1
                i -= 1
                while j >= 0 and (i, j) not in seen:
                    res.append(matrix[i][j])
                    seen.add((i, j))
                    j -= 1
                go_left = False
                go_up = True
            elif go_up:
                j += 1
                i -= 1
                while i >= 0 and (i, j) not in seen:
                    res.append(matrix[i][j])
                    seen.add((i, j))
                    i -= 1
                go_up = False
                go_right = True
        return res

