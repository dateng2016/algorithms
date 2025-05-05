from typing import List
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distances = [0] + [float("inf")] * n
        distances[k] = 0
        q = []
        heapq.heappush(q, (0, k))
        while q:
            _, source = heapq.heappop(q)
            for nei, weight in graph[source]:
                if distances[nei] > distances[source] + weight:
                    distances[nei] = distances[source] + weight
                    heapq.heappush(q, (distances[nei], nei))

        return max(distances[1:]) if float("inf") not in distances else -1
