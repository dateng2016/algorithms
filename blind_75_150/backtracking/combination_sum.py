from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # R -> O(n ** target)
        # S -> O( memory of result + target ** 2????? )
        seen = set()
        res = []
        l = len(candidates)

        def dfs(idx, ls, s):
            # The sum of ls is for sure smaller than the target
            for i in range(idx, l):
                if s + candidates[i] == target:
                    res.append(ls + [candidates[i]])
                elif s + candidates[i] < target:
                    dfs(i, ls + [candidates[i]], s + candidates[i])

        for i in range(len(candidates)):
            if candidates[i] in seen:
                continue
            seen.add(candidates[i])
            if candidates[i] < target:
                dfs(i, [candidates[i]], candidates[i])
            elif candidates[i] == target:
                res.append([candidates[i]])
        return res

