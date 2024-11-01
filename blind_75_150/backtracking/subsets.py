from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        R -> 2 ** n   Since for each element we can decide to include it or not include it
        S -> 2 ** n   To store all the result
        """
        res = [[]]
        l = len(nums)

        def dfs(idx, cur):
            res.append(cur)
            for i in range(idx + 1, l):
                dfs(i, cur + [nums[i]])

        for i in range(l):
            dfs(i, [nums[i]])
        return res


sol = Solution()
nums = [1, 2, 3]
res = sol.subsets(nums)
print(res)

