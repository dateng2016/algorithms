from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution 2: Bit Manipulation
        ans = 0
        for i in range(len(nums) + 1):
            ans ^= i
        for n in nums:
            ans ^= n
        return ans

        # Solution 1
        l = len(nums)
        nums.append(1)
        zero_reversed = False

        for i in range(l):
            idx_to_reverse = nums[i]
            nums[abs(idx_to_reverse)] *= -1
            if nums[abs(idx_to_reverse)] == 0:
                zero_reversed = True

        for i in range(l + 1):
            if nums[i] > 0:
                return i
            elif nums[i] == 0 and not zero_reversed:
                return i

