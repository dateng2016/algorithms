from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy_head = ListNode()
        previous_tail = dummy_head
        # * Let's do a count before reversing
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        last_idx = (count // k) * k
        idx = 1
        prev = dummy_head
        cur = head
        tail_on_hold = None
        while idx <= last_idx:
            remainder = idx % k
            if remainder == 1:
                # * This node will become the previous tail in the future
                # * We will let it become the prev_tail officially once we find the head
                tail_on_hold = cur
                # * We do not flip its pointer YET
                nxt_node = cur.next
                prev = cur
                cur = nxt_node

            elif remainder == 0:
                # * We have found the head for this group now:
                # * Now we know where the tail should be pointing to
                nxt_node = cur.next
                tail_on_hold.next = nxt_node
                previous_tail.next = cur
                cur.next = prev
                prev = cur
                cur = nxt_node
                previous_tail = tail_on_hold
            else:
                nxt_node = cur.next
                cur.next = prev
                prev = cur
                cur = nxt_node
            idx += 1
        return dummy_head.next


def print_nodes(head: ListNode):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


for i in range(1, 6):
    stmt = f"node{i} = ListNode({i})"
    exec(stmt)
for i in range(1, 5):
    stmt = f"node{i}.next = node{i + 1}"
    exec(stmt)

node1: ListNode
print_nodes(node1)


print()
sol = Solution()
res = sol.reverseKGroup(node1, 3)

print_nodes(res)


s = "Reverse Nodes in k-Group.py".lower()
ls = s.split(" ")
print("_".join(ls))

