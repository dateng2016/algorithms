from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        R -> O(n)
        S -> O(n)
        """
        if not head:
            return None
        old_cur = head
        new_head = Node(x=head.val)
        new_cur = new_head
        old_node_to_new_node = dict()
        old_node_to_new_node[old_cur] = new_cur
        while old_cur.next:
            new_cur.next = Node(x=old_cur.next.val)
            old_cur = old_cur.next
            new_cur = new_cur.next
            old_node_to_new_node[old_cur] = new_cur
        old_cur = head
        new_cur = new_head
        while old_cur:
            if old_cur.random:
                new_cur.random = old_node_to_new_node[old_cur.random]
            old_cur = old_cur.next
            new_cur = new_cur.next
        return new_head


s = "Copy List with Random Pointer.py".lower()
ls = s.split(" ")
print("_".join(ls))

