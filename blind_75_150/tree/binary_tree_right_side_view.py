from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen_levels = set()
        res = []

        def helper(node: Optional[TreeNode], level: int):
            if not node:
                return
            if level not in seen_levels:
                seen_levels.add(level)
                res.append(node.val)
            helper(node.right, level + 1)
            helper(node.left, level + 1)

        helper(root, 1)
        return res


s = "Binary Tree Right Side View.py".lower()
ls = s.split(" ")
print("_".join(ls))

