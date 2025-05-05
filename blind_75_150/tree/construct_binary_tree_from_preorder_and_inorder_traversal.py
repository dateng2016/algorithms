from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # NeetCode Guy: Recursive Approach (Mine performs better actually)
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(
            preorder=preorder[1 : mid + 1], inorder=inorder[:mid]
        )
        root.right = self.buildTree(
            preorder=preorder[mid + 1 :], inorder=inorder[mid + 1 :]
        )
        return root

        # R -> O(n)
        # S -> O(n)

        root = TreeNode(val=preorder[0])
        seen = set()
        seen.add(root.val)
        # Use the preorder to construct left nodes until it sees the
        # in_order node that we are currenty pointing to
        i = 1
        j = 0
        cur = root

        if inorder[0] == preorder[0]:
            right = True
            j += 1
        else:
            right = False

        # We need a list to keep track of the nodes to work on
        ls = [root]

        while i < len(preorder):
            seen.add(preorder[i])
            nxt = TreeNode(val=preorder[i])  # Next node to append
            ls.append(nxt)
            if right:
                cur.right = nxt
            else:
                cur.left = nxt
            if preorder[i] == inorder[j]:
                right = True
                while j < len(inorder) and inorder[j] in seen:
                    j += 1
                target = None
                while not target or target.val != inorder[j - 1]:
                    target = ls.pop()
                    cur = target
            else:
                right = False
                cur = nxt
            i += 1
        return root
