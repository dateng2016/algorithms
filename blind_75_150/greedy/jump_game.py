from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Need to check if there is a 0.
        If there is 0, we need to check if possible to
        escape that 0
        R -> O(n)
        S -> O(1)
        """
        if 0 not in nums:
            return True
        if nums[0] == 0 and len(nums) > 1:
            return False
        # zero_idxs = []
        zero_idx = None
        i = len(nums) - 1
        while i > 0:
            # If we reach to idx 0, we can do it
            if nums[i] == 0:
                zero_idx = i
                while i >= 0:
                    i -= 1
                    if nums[i] > (zero_idx - i) or (
                        nums[i] == (zero_idx - i) and zero_idx == len(nums) - 1
                    ):
                        break
                if i < 0:
                    return False
                else:
                    continue
            i -= 1
        return True

