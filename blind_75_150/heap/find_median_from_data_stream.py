import heapq


class MedianFinder:

    def __init__(self):
        # * We want to be able to pop its max value, so we keep NEGATIVE value
        self.smaller_arr = []
        # * We want to be able to pop its min value, we keep POSITIVE, we make this the LARGER array
        self.bigger_arr = []

    def addNum(self, num: int) -> None:
        # * We need to make sure which array to add it to
        if not self.bigger_arr:
            heapq.heappush(self.bigger_arr, num)
            return
        totol_length = len(self.bigger_arr) + len(self.smaller_arr)
        # * If total_length is odd -> it WILL be EVEN,
        if totol_length % 2 == 1:
            prev_bigger = heapq.heappop(self.bigger_arr)
            smaller = min(num, prev_bigger)
            bigger = max(num, prev_bigger)
            heapq.heappush(self.smaller_arr, -smaller)
            heapq.heappush(self.bigger_arr, bigger)
        else:
            # * total_length is even -> it WILL be ODD
            prev_neg_smaller = heapq.heappop(self.smaller_arr)
            prev_smaller = -prev_neg_smaller
            smaller = min(num, prev_smaller)
            bigger = max(num, prev_smaller)
            heapq.heappush(self.smaller_arr, -smaller)
            heapq.heappush(self.bigger_arr, bigger)

    def findMedian(self) -> float:
        totol_length = len(self.bigger_arr) + len(self.smaller_arr)
        if totol_length % 2 == 1:
            ans = heapq.heappop(self.bigger_arr)
            heapq.heappush(self.bigger_arr, ans)
            return ans
        neg_smaller_num = heapq.heappop(self.smaller_arr)
        bigger_num = heapq.heappop(self.bigger_arr)
        heapq.heappush(self.smaller_arr, neg_smaller_num)
        heapq.heappush(self.bigger_arr, bigger_num)
        smaller_num = -neg_smaller_num
        return (smaller_num + bigger_num) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

