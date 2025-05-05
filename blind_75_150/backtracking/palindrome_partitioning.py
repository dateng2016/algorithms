from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pali(s):
            return s == s[::-1]

        def dfs(idx: int, cur: List):
            # * idx has NOT been used yet
            if idx == len(s):
                res.append(cur)
            for i in range(idx, len(s)):
                if is_pali(s[idx : i + 1]):
                    dfs(i + 1, cur + [s[idx : i + 1]])

        dfs(0, [])
        return res

