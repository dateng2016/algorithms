from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Note this is a binary SEARCH tree
        # R -> O(log n)
        # NEETCODE GUY
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                # Current value is too small
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

        # R -> at least O(n) since we need to traverse the entire tree
        #       for the worst case any ways
        res = None

        def helper(node: TreeNode):
            nonlocal res
            if res:
                return False, False
            contains_p = contains_q = False
            if not node:
                return False, False

            left_result = helper(node.left)
            right_result = helper(node.right)

            if node == p:
                contains_p = True

                _, contains_q = (
                    left_result[0] or right_result[0],
                    left_result[1] or right_result[1],
                )
            elif node == q:
                contains_q = True
                contains_p, _ = (
                    left_result[0] or right_result[0],
                    left_result[1] or right_result[1],
                )
            else:
                contains_p, contains_q = (
                    left_result[0] or right_result[0],
                    left_result[1] or right_result[1],
                )
            if contains_p and contains_q:
                res = node
                return False, False
            else:
                return contains_p, contains_q

        helper(root)
        return res

