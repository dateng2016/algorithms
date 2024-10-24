from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # NeetCode Guy: Two Pointers
        # R-> O(n**2), Space-> O(n) due to python sorting
        seen = set()
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            first = nums[i]
            if first in seen:
                continue
            seen.add(first)
            l = i + 1
            r = len(nums) - 1
            target = 0 - first
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([first, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res

        # We traverse the counter twice -> O(n*2)
        res = set()
        count = Counter(nums)
        keys = list(count.keys())
        for i in range(len(keys)):
            k1 = keys[i]
            c1 = count[k1]
            for j in range(i, len(keys)):
                k2 = keys[j]
                c2 = count[k2]

                if k1 == k2:
                    if c1 == 1:
                        continue
                    else:
                        target = 0 - k1 - k2
                        if target == 0:
                            if c1 >= 3:
                                res.add((0, 0, 0))
                        elif target in keys:
                            res.add(tuple(sorted([k1, k2, target])))
                else:
                    target = 0 - k1 - k2
                    if target == k1 and c1 >= 2:
                        res.add(tuple(sorted([k1, k1, k2])))
                    elif target == k2 and c2 >= 2:
                        res.add(tuple(sorted([k1, k2, k2])))
                    elif target in keys and target != k1 and target != k2:
                        res.add(tuple(sorted([k1, k2, target])))
        res = list(res)
        return list(map(list, res))

        # Brute force: Traverse the entire list three times
        # R -> O(n**3)
        res = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(res)

