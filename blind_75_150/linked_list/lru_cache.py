from typing import Optional, Dict


class Node:
    def __init__(
        self, val=0, left: Optional["Node"] = None, right: Optional["Node"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class LRUCache:
    """
    R -> O(1) for each
    S -> O(n)
    """

    def __init__(self, capacity: int):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.right = self.dummy_tail
        self.dummy_tail.left = self.dummy_head
        self.key_to_node: Dict[int, Node] = dict()
        self.node_to_key: Dict[Node, int] = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node: Node = self.key_to_node[key]
        # * We need to delete it from the original location
        node.left.right = node.right
        node.right.left = node.left
        # * We need to append it before the dummy_tail
        last_node = self.dummy_tail.left
        last_node.right = node
        node.left = last_node
        self.dummy_tail.left = node
        node.right = self.dummy_tail

        return node.val

    def put(self, key: int, value: int) -> None:
        # * If the key already EXISTS, we merely update the value
        if key in self.key_to_node:
            current_node = self.key_to_node[key]
            current_node.val = value
            # * We need to move it to the last node
            # * First we delete the current node
            current_node.left.right = current_node.right
            current_node.right.left = current_node.left
            # * We insert it to the last node
            last_node = self.dummy_tail.left
            last_node.right = current_node
            current_node.left = last_node

            self.dummy_tail.left = current_node
            current_node.right = self.dummy_tail
            return
        # * It does NOT exist, we create a new one
        node = Node(val=value)
        self.key_to_node[key] = node
        self.node_to_key[node] = key
        # * Now we put this at the end of the linked list before the tail
        last_node = self.dummy_tail.left
        last_node.right = node
        node.left = last_node

        node.right = self.dummy_tail
        self.dummy_tail.left = node

        # * We need to check whether it exceeds the capacity
        if len(self.key_to_node) > self.capacity:
            # * Pop the first node
            first_node = self.dummy_head.right
            self.dummy_head.right = first_node.right
            first_node.right.left = self.dummy_head
            key = self.node_to_key[first_node]
            del self.node_to_key[first_node]
            del self.key_to_node[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 2 -> 1
# 1 -> 1
# 2 -> 3
# 4 -> 1

