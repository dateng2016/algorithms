from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # R -> at least O(n) since we need to traverse the entire thing
        # S -> at least O(n) since we need to obtain the entire thing
        res = []

        def search(node: TreeNode, level: int):
            if not node:
                return
            elif level > len(res):
                res.append([node.val])
            else:
                res[level - 1].append(node.val)
            search(node.left, level + 1)
            search(node.right, level + 1)

        search(root, 1)
        return res

