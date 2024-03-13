# Definition for a binary tree node.
import collections
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = collections.deque()
        
        if root:
            q.append(root)

        while q:
            length_q = len(q)
            val = []

            for i in range(length_q):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(val)
        
        return ans
