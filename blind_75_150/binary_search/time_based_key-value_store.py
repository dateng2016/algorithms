from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """Here we need to do a binary search"""
        arr = self.hash_map[key]
        # * First we consider the edge cases where we return ""
        if not arr or arr[0][0] > timestamp:
            return ""
        # * Another edge case -> When we can just return the last element
        if arr[-1][0] <= timestamp:
            return arr[-1][1]
        # * We want to find the first timestamp that is <= "timestamp"
        # * The target condition is   arr[mid] <= timestamp <arr[mid + 1]
        # * Since the targeting index can only be in the range [1, len() - 2]
        left = 0
        right = len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp < arr[mid + 1][0]:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                # * This means that we need to move towards left
                right = mid - 1
            else:
                left = mid + 1
        # return arr[mid][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


s = "Time Based Key-Value Store.py".lower()
ls = s.split(" ")
print("_".join(ls))

