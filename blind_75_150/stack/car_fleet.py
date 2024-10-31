from typing import List
from collections import defaultdict


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        # * TRIAL 2
        # * Elements in positions are UNIQUE
        # * Optimize the memory a little bit
        # position_to_finishing_time = dict()
        positions_and_fin_times = []
        for i in range(len(positions)):

            positions_and_fin_times.append(
                (positions[i], (target - positions[i]) / speeds[i])
            )
        # * Fleet forms in this way:
        # * Car A has a greater position than the Car B AND Car A 's finishing_time >= Car B
        # * Each car fleet has a max_starting_position and a max_finishing_time
        positions_and_fin_times.sort(reverse=True)
        cur_min_finishing_time = -float("inf")
        ans = 0
        for p, f in positions_and_fin_times:
            if f > cur_min_finishing_time:
                ans += 1
                cur_min_finishing_time = f
        return ans

        # * Elements in positions are UNIQUE
        position_to_finishing_time = dict()
        for i in range(len(positions)):
            position_to_finishing_time[positions[i]] = (target - positions[i]) / speeds[
                i
            ]
        # * Fleet forms in this way:
        # * Car A has a greater position than the Car B AND Car A 's finishing_time >= Car B
        # * Each car fleet has a max_starting_position and a min_finishing_time
        positions.sort(reverse=True)
        cur_min_finishing_time = -float("inf")
        ans = 0
        for p in positions:
            if position_to_finishing_time[p] > cur_min_finishing_time:
                ans += 1
                cur_min_finishing_time = position_to_finishing_time[p]
        return ans


target = 12
positions = [10, 8, 0, 5, 3]
speeds = [2, 4, 1, 1, 3]
sol = Solution()
res = sol.carFleet(target, positions, speeds)
print(res)

