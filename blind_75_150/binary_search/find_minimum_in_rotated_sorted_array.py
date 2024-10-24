from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We want to find the index i such that nums[i] < nums[i - 1]
        # edge case: NOT rotated. i = 0
        # We take two references from
        # the BEGINNING and the END
        if len(nums) == 1:
            return nums[0]
        left = nums[0]
        right = nums[-1]
        if left < right:
            return left
        if nums[-1] < nums[-2]:
            return nums[-1]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            # NOTE: We need to do this check because
            #       it is not it cannot satisfy none of the three conditions
            if mid == 0:
                l = mid + 1
                continue

            elif mid == len(nums) - 1:
                r = mid - 1
                continue

            # Perform the condition check
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            elif nums[mid] > left:
                l = mid + 1

            elif nums[mid] < right:
                r = mid - 1

