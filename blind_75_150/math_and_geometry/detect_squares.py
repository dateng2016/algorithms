
from typing import List
from collections import defaultdict

class DetectSquares:

    # * GPT Approach
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        for (px, py), count_diagonal in self.points.items():
            # Only consider points that can be diagonal of a square
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            # The other two corners of the square
            count1 = self.points.get((x, py), 0)
            count2 = self.points.get((px, y), 0)
            total += count_diagonal * count1 * count2
        return total


# class DetectSquares:

#     def __init__(self):
#         # * row/col -> a point_count dictionary
#         self.row_dict = defaultdict(lambda: defaultdict(int))
#         self.col_dict = defaultdict(lambda: defaultdict(int))

#     def add(self, point: List[int]) -> None:
#         row, col = point
#         self.row_dict[row][tuple(point)] += 1
#         self.col_dict[col][tuple(point)] += 1

#     def count(self, point: List[int]) -> int:
#         # * Traverse through the row
#         row, col_1 = point
#         point_count_for_row = self.row_dict[row]
#         ans = 0
#         for point_on_same_row in point_count_for_row:
#             col_2 = point_on_same_row[1]
#             distance = abs(col_2 - col_1)
#             if not distance:
#                 # * Overlap Point -> Skip
#                 continue
#             point_count_for_col_1 = self.col_dict[col_1]
#             point_count_for_col_2 = self.col_dict[col_2]
#             # * Look Above
#             third_point_1 = (row + distance, col_1)
#             fourth_point_1 = (row + distance, col_2)
#             ans += (
#                 point_count_for_col_1[third_point_1]
#                 * point_count_for_col_2[fourth_point_1]
#             )

#             # * Look Below
#             third_point_2 = (row - distance, col_1)
#             fourth_point_2 = (row - distance, col_2)
#             ans += (
#                 point_count_for_col_1[third_point_2]
#                 * point_count_for_col_2[fourth_point_2]
#             )
#         return ans


# # Your DetectSquares object will be instantiated and called as such:
# # obj = DetectSquares()
# # obj.add(point)
# # param_2 = obj.count(point)
