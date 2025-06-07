from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(queries)
        answer_map = dict()
        min_heap = []
        idx = 0

        for q in sorted_queries:
            # Push all intervals where left <= q
            while idx < len(intervals) and intervals[idx][0] <= q:
                l, r = intervals[idx]
                heapq.heappush(min_heap, (r - l + 1, r))
                idx += 1

            # Pop all intervals from heap where right < q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # The top of the heap is the smallest interval that covers q
            if min_heap:
                answer_map[q] = min_heap[0][0]
            else:
                answer_map[q] = -1

        # Prepare result in original query order
        return [answer_map[q] for q in queries]
