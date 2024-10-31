from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # * NEETCODE GUY
        slow = fast = 0
        print(slow, fast)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                break
        slow2 = 0
        print("-----")
        print(slow, slow2)
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            print(slow, slow2)
            if slow == slow2:
                return slow


# * We have n + 1 elements  ->  index range [0, n]
# * We elements of range [1, n]
# *
# *
# *  2 1 3 4 2

# * 0 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4
# * In here 0 is like a dummy_head that is NEVER in the cycle

sol = Solution()
nums = [2, 1, 3, 4, 2]
res = sol.findDuplicate(nums)
# print(res)


s = "Find the Duplicate Number.py".lower()
ls = s.split(" ")
print("_".join(ls))

