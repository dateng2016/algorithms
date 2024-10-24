from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # S -> O(1)
        # R -> O(min(length1, length2))

        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        arr1, arr2 = nums1, nums2
        if len(arr2) < len(arr1):
            arr1, arr2 = arr2, arr1
        l, r = 0, len(arr1) - 1
        while True:
            mid_1 = (l + r) // 2
            mid_2 = half - mid_1 - 2

            arr1_left = arr1[mid_1] if mid_1 >= 0 else -float("inf")
            arr2_left = arr2[mid_2] if mid_2 >= 0 else -float("inf")
            arr1_right = arr1[mid_1 + 1] if mid_1 + 1 < len(arr1) else float("inf")
            arr2_right = arr2[mid_2 + 1] if mid_2 + 1 < len(arr2) else float("inf")

            if arr1_left <= arr2_right and arr2_left <= arr1_right:
                # We found the solution
                if total_length % 2 == 1:
                    return min(arr1_right, arr2_right)
                else:
                    return (max(arr1_left, arr2_left) + min(arr1_right, arr2_right)) / 2

            elif arr1_left > arr2_right:
                # this means that a1 is too big
                r = mid_1 - 1
            else:
                l = mid_1 + 1

