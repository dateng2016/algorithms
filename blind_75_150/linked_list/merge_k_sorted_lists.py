from typing import List, Optional, Tuple
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, nodes_list: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq: List[Tuple[int, ListNode]] = []
        dummy_num = 0
        for node in nodes_list:
            if not node:
                continue
            heapq.heappush(pq, (node.val, dummy_num, node))
            dummy_num += 1
        dummy_head = ListNode()
        cur = dummy_head
        while pq:
            _, _, node = heapq.heappop(pq)
            cur.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, dummy_num, node.next))
                dummy_num += 1
            cur = cur.next
        return dummy_head.next


s = "Merge k Sorted Lists.py".lower()
ls = s.split(" ")
print("_".join(ls))

