from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # NeetCode Guy Solution
        # This gets us R: O(n)
        if not nums:
            return 0
        nums_set = set(nums)
        checked = set()
        ans = 1
        for n in nums_set:
            count = 1
            if n in checked:
                continue
            cur = n
            while cur + 1 in nums_set:
                count += 1
                checked.add(cur + 1)
                cur += 1
            cur = n
            while cur - 1 in nums_set:
                count += 1
                checked.add(cur - 1)
                cur -= 1
            ans = max(ans, count)
        return ans

        # This is my approach, maybe it needs correction
        # Optimize it to run it in O(n)
        # dictionary key = number, value = [min_number that it connects to, max_number, length]
        # When updating, we also update the length of its min_number and max_number

        if not nums:
            return 0
        d = defaultdict(lambda: [0, 0, 0])
        ans = 0
        nums = set(nums)
        for n in nums:
            if d[n][-1]:
                continue
            d[n][0] = d[n][1] = n
            d[n][-1] = 1
            d[n][-1] += d[n - 1][-1]
            d[n][-1] += d[n + 1][-1]

            if d[n - 1][-1]:
                d[n - 1][-1] = d[n][-1]
                d[n][0] = d[n - 1][0]
                min_number = d[n][0]
                # We update the min_number
                d[min_number][-1] = d[n][-1]
                d[n - 1][1] = d[n][1]
            if d[n + 1][-1]:
                d[n + 1][-1] = d[n][-1]
                d[n][1] = d[n + 1][1]
                max_number = d[n][1]
                # We update the min_number
                d[max_number][-1] = d[n][-1]
                d[n + 1][0] = d[n][0]
            ans = max(ans, d[n][-1])
            print(d)
        return ans
        # Brute force, sort it! R: O(n log(n))

        if not nums:
            return 0
        nums.sort()
        cur = 1
        ans = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            elif nums[i] == prev + 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 1
            prev = nums[i]
        return ans

        pass


