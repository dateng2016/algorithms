from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        R -> O(n)
        S -> O(n)
        """

        if not intervals:
            return [newInterval]

        def has_overlap(arr1: List, arr2: List) -> bool:
            if arr1[0] > arr2[1] or arr2[0] > arr1[1]:
                return False
            return True

        res = []
        added = False
        cur_min, cur_max = newInterval
        for interval in intervals:
            # Non overlap
            if interval[1] < newInterval[0]:
                # This means that the current interval is smaller
                # the new interval
                res.append(interval)
            elif interval[0] > newInterval[1]:
                # This means that the current interval is greater
                # than the new interval
                if not added:
                    # If we have not added the new interval, we need
                    # to add it first
                    res.append([cur_min, cur_max])
                    added = True
                res.append(interval)

            else:
                # There is some overlap

                cur_min = min(cur_min, interval[0])
                cur_max = max(cur_max, interval[1])
        if not added:
            res.append([cur_min, cur_max])
        return res

