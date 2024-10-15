
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def construct_list_nodes(arr: List) -> ListNode:
    head = ListNode(arr[0])

    cur = head
    i = 1
    while i < len(arr):
        cur.next = ListNode(arr[i])
        cur = cur.next
        i += 1
    return head


def output_list_from_node(head: ListNode) -> List:
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print(arr)


arr = [1, 2, 3, 4, 5]
head = construct_list_nodes(arr)
output_list_from_node(head)

