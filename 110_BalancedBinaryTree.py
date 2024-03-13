from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: 
    def BalancedBinaryTree(self, root:Optional[TreeNode]) -> bool:
        return self.height(root) >= 0

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
