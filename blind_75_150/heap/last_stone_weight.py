from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-w for w in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)
            if heaviest == second_heaviest:
                continue
            heapq.heappush(stones, -(heaviest - second_heaviest))
        return -stones[0] if stones else 0

