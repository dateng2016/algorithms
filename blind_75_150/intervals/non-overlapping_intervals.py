from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # We iterate through the whole thing
        # When overlaps detected, we remove the one
        # with larger max value
        if len(intervals) <= 1:
            return 0
        cur_min, cur_max = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            if not (left >= cur_max or right <= cur_min):

                ans += 1
                # If overlap
                # We get rid of the one that has a greater maximum
                if right < cur_max:
                    # This means that we need to get rid of the previous one
                    cur_min = left
                    cur_max = right
            else:
                # There is no overlap
                cur_min, cur_max = left, right
        return ans

