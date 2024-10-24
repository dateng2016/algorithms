from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        R -> O(n log n) account for the sorting
        S -> O(n) Also need to account for both "res" and sorting
        """
        intervals.sort()
        if len(intervals) <= 1:
            return intervals
        cur_min, cur_max = intervals[0]
        added_cur = False
        res = []
        for interval in intervals:
            left, right = interval
            # If it has overlap, then we update
            if cur_min <= left <= cur_max or cur_min <= right <= cur_max:
                cur_min = min(cur_min, left)
                cur_max = max(cur_max, right)
            else:
                # There is no overlap
                res.append([cur_min, cur_max])
                cur_min, cur_max = interval
        res.append([cur_min, cur_max])

        return res


s = Solution()
intervals = [[1, 4], [4, 5]]
result = s.merge(intervals=intervals)
print(result)

