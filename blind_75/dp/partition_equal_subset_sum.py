from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # R -> O(n ** 2)
        # S -> O(n ** 2)
        # DP
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        possible_sums = {0}
        for n in nums:
            to_adds = set()
            for s in possible_sums:
                if n + s == target:
                    return True
                elif n + s < target:
                    to_adds.add(n + s)
            for to_add in to_adds:
                possible_sums.add(to_add)
        return False

        # R -> O(n * sum(nums))
        # S -> O(n * sum(nums))
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        ans = False

        def helper(idx, target):
            nonlocal ans
            if ans:
                return

            for i in range(idx + 1, len(nums)):
                if target - nums[i] == 0:
                    ans = True
                    return
                elif target - nums[i] > 0:
                    helper(i, target - nums[i])
                helper(i, target)

        helper(0, target - nums[0])
        helper(0, target)

        return ans

