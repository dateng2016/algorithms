import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle_length = n + 1
        pq = []
        task_frequency = Counter(tasks)
        for frequency in task_frequency.values():
            heapq.heappush(pq, -frequency)
        ans = 0

        while pq:
            neg_freq_holder = []
            timer = cycle_length
            while timer:
                if pq:
                    timer -= 1
                    ans += 1
                    neg_frequency = heapq.heappop(pq)
                    neg_frequency += 1
                    neg_freq_holder.append(neg_frequency)
                else:
                    break
            # print(timer, ans)
            for neg_frequency in neg_freq_holder:
                if neg_frequency:
                    heapq.heappush(pq, neg_frequency)
            if pq:
                ans += timer
        return ans

