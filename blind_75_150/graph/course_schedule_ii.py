from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        before_to_after = defaultdict(list)
        num_prereqs = defaultdict(int)
        for after, before in prerequisites:
            before_to_after[before].append(after)
            num_prereqs[after] += 1
        q = deque()
        for course in range(numCourses):
            if num_prereqs[course] == 0:
                q.append(course)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for nxt_course in before_to_after[course]:
                num_prereqs[nxt_course] -= 1
                if num_prereqs[nxt_course] == 0:
                    q.append(nxt_course)
        return res if len(res) == numCourses else []

