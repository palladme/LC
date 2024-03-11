# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, seq = None):
        self.head = None
        if seq:
            for val in reversed(seq):
                self.head = ListNode(val, self.head)

class Solution:
    def ReorderList(head: Optional[ListNode]) -> None:
        
        # Find middle of list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
                
        # Merge two list
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

# Testing
test1_vals = [1,2,3,4]
test1_expected = [1,4,2,3]

test1_list = LinkedList()
test1_list_node = ListNode(test1_vals[0])
test1_list.head = test1_list_node

for val in test1_vals[1:]:
    test1_list_node.next = ListNode(val)
    test1_list_node = test1_list_node.next

# Output of actual
Solution.ReorderList(test1_list.head)
test1_actual = []
curr = test1_list.head

while curr:
    test1_actual.append(curr.val)
    curr = curr.next

# Compare expected with actual
assert len(test1_expected) == len(test1_actual), f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
for i in range(len(test1_expected)):
    assert(test1_expected[i] == test1_actual[i]), f"The actual result does not match all values for the expected result."




