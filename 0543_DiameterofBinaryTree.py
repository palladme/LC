# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1

        depth(root)

        return self.res
