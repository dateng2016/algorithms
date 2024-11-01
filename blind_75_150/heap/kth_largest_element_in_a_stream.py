from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # * You only want to keep k elements that are the largest
        self.k = k
        self.scores = nums
        # self.scores.sort(reverse=True)
        # self.scores = self.scores[:k]  # * We keep the k-largest elements in there
        heapq.heapify(self.scores)

        # * NEETCODE GUY APPROACH (different from comments above)
        while len(self.scores) > k:
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        if len(self.scores) == self.k:
            # * It has JUST had enough elements in there
            ans = heapq.heappop(self.scores)
            heapq.heappush(self.scores, ans)
            return min(self.scores)
        elif len(self.scores) == self.k + 1:
            # * It ALREADY had enough before. Now it EXCEEDED
            # * We need to POP one element -> THEN return the min
            heapq.heappop(self.scores)
            ans = heapq.heappop(self.scores)
            heapq.heappush(self.scores, ans)
            return ans
        # * Return the smallest score in the array


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

