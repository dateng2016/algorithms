from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def dfs(idx, cur):
            res.append(cur)
            prev = None
            for i in range(idx + 1, len(nums)):
                if prev == nums[i]:
                    continue
                prev = nums[i]
                dfs(i, cur + [nums[i]])

        prev = None
        for i in range(len(nums)):
            if prev == nums[i]:
                continue
            prev = nums[i]
            dfs(i, [nums[i]])
        return res


sol = Solution()
res = sol.subsetsWithDup([1, 2, 2])
print(res)

