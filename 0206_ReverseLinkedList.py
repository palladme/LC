# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

from typing import List

class Solution:
    def ReverseLinkedList(head: List[int]) -> List[int]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, seq=None):
        self.head = None
        if seq is not None:
            for val in reversed(seq):
                self.head = ListNode(val, self.head)

# Test 1
test1_vals = [1,2,3,4,5]
test1_expected = [5,4,3,2,1]

test1_List = LinkedList()
node1 = ListNode(test1_vals[0])
test1_List.head = node1
for val in test1_vals[1:]:
    node1.next = ListNode(val)
    node1 = node1.next

solution_1 = Solution.ReverseLinkedList(test1_List.head)
curr = solution_1
test1_actual = []

while curr:
    test1_actual.append(curr.val)
    curr = curr.next

assert len(test1_expected) == len(test1_actual), f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
for i in range(len(test1_expected)):
    assert(test1_expected[i] == test1_actual[i]), f"The actual result does not match all values for the expected result."

# Test 2
test2_vals = [1,2]
test2_expected = [2,1]
test2_List = LinkedList()
node2 = ListNode(test2_vals[0])
test2_List.head = node2
for val in test2_vals[1:]:
    node2.next = ListNode(val)
    node2 = node2.next

solution_2 = Solution.ReverseLinkedList(test2_List.head)
curr = solution_2
test2_actual = []

while curr:
    test2_actual.append(curr.val)
    curr = curr.next

assert len(test2_expected) == len(test2_actual), f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
for i in range(len(test2_expected)):
    assert(test2_expected[i] == test2_actual[i]), f"The actual result does not match all values for the expected result."


# Test 3
test3_head = []
test3_expected = []
test3_vals = [1,2]
test3_expected = [2,1]
test3_List = LinkedList()
node3 = ListNode(test3_vals[0])
test3_List.head = node3
for val in test3_vals[1:]:
    node3.next = ListNode(val)
    node3 = node3.next

solution_3 = Solution.ReverseLinkedList(test3_List.head)
curr = solution_3
test3_actual = []

while curr:
    test3_actual.append(curr.val)
    curr = curr.next

assert len(test3_expected) == len(test3_actual), f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
for i in range(len(test3_expected)):
    assert(test3_expected[i] == test3_actual[i]), f"The actual result does not match all values for the expected result."
