from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Let the length of the prerequisites list to be p
        # Let the numCourses be n
        # R -> O(p + n)
        # S -> O(p + n)
        num_prqt = defaultdict(int)
        after_to_before = {}
        before_to_after = defaultdict(list)
        for after, before in prerequisites:  # This is R -> O(p)
            after_to_before[after] = before
            num_prqt[after] += 1
            before_to_after[before].append(after)
        count = 0
        q = deque()
        for i in range(numCourses):
            if not num_prqt[i]:
                q.append(i)
        if not q:
            return False
        while q:  # This is R -> O(n) because it can pop n times at most
            target = q.popleft()
            count += 1
            for after in before_to_after[target]:
                num_prqt[after] -= 1
                if not num_prqt[after]:
                    q.append(after)

        return count == numCourses

