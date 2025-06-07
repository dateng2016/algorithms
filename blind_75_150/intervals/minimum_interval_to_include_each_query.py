from typing import List
from collections import defaultdict


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # * Brute Force Way -> Runtime Complexity O(m * n)



        # * Maintain 2 sorted list -> 
        # * - Based on the first element 
        # * - Based on the second element
        # * During the query, check both, find out the one that requires the least check????
        pass
