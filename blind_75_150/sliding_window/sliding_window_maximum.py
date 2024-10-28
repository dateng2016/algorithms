from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # * NEETCODE GUY SOLUTION R -> O(n) S -> O(n)
        res = []
        dq = deque()
        # * Initializing out deque
        for i in range(k):  # * This is the starting array
            n = nums[i]
            if not dq:
                dq.append(n)
            elif dq[0] < n:
                dq = deque([n])
            else:
                while dq[-1] < n:
                    dq.pop()
                dq.append(n)
        i = 0
        j = k - 1

        while j < len(nums):
            # print(dq)
            res.append(dq[0])
            if dq[0] == nums[i]:
                dq.popleft()
            i += 1
            j += 1
            while j < len(nums) and dq and dq[-1] < nums[j]:
                dq.pop()
            if j < len(nums):
                dq.append(nums[j])
        return res

        # * First we initialize the first array nums[0:k] -> its find its max() as prev_max
        # * We slide the window, if the element added > prev_max -> append new_max and update prev_max
        # * elif the element deleted IS the prev_max and count[prev_max_key] == 0 -> We need a new max
        # * WHAT WE WANT
        # * Something to store current data, adding and deleting fast, get the current_max fast
        res = []
        i = 0
        j = i + k
        arr = [-n for n in nums[i:j]]
        # * This "arr" keeps elements of [i, j - 1]
        heapq.heapify(arr)
        count = Counter(nums[i:j])
        while j <= len(nums):
            # print(nums[i:j], end=" ")
            possible_max = -heapq.heappop(arr)
            while not count[possible_max]:
                possible_max = -heapq.heappop(arr)
            res.append(possible_max)
            heapq.heappush(arr, -possible_max)
            count[nums[i]] -= 1
            i += 1
            if j < len(nums):
                count[nums[j]] += 1
                heapq.heappush(arr, -nums[j])
            j += 1
            # print(res)

        return res


sol = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
print(res)

