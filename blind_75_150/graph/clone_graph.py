from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # n is the number of vertices, e is the number of edges
        # R -> O(n + e), for each edge, the neighbor.append operation runs twice
        # S -> O(n), the max length of the call stack is n, also n keys/values in the dict

        if not node:
            return node

        old_to_new = dict()

        def clone(node: Node):
            # This function clone the node via dfs method
            if node in old_to_new:
                return old_to_new[node]
            new_node = Node(node.val)
            old_to_new[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))
            return new_node

        return clone(node)

