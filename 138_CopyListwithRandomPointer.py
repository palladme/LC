# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


# Definition for a Node.

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def CopyListwithRandomPointer(head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None 
        
        copy_hm = {}

        curr = head
        while curr:
            copy_hm[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy_hm[curr].next = copy_hm.get(curr.next)
            copy_hm[curr].random = copy_hm.get(curr.random)
            curr = curr.next
        
        return copy_hm[head]
