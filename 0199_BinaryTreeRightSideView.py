# Definition for a binary tree node.
from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = collections.deque([root])

        while q:
            rightside = None
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()

                if node:
                    rightside = node
                    q.append(node.left)    
                    q.append(node.right)
            if rightside:
                ans.append(rightside.val)
        
        return ans
