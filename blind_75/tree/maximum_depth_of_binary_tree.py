from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Not much improvement for R and S
        # Iterative DFS
        if not root:
            return 0
        stack: List[List[TreeNode, int]] = [[root, 1]]
        ans = 1
        while stack:
            node, level = stack.pop()
            ans = max(level, ans)
            if node.left:
                stack.append([node.left, level + 1])
            if node.right:
                stack.append([node.right, level + 1])
        return ans
        # Iterative BFS
        # Same R -> O(n)
        #       S -> O(1) for best case
        #         -> O(2 ** (log(n) - 1)) which is O(n) for worst case
        q: deque[TreeNode] = deque()
        level = 0
        if not root:
            return level
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

        # Recursive solution: R -> O(n) this will always be true since we
        #                       need to check all the nodes
        #                   S -> O(log n) for balanced tree (account for call stack)
        #                       O(n) for worst case
        ans = 0

        if not root:
            return ans

        def helper(node: Optional[TreeNode], level: int):
            if not node:
                nonlocal ans
                ans = max(ans, level - 1)
                return
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 1)
        return ans

