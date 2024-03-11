# Example 1
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

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
    def MergeTwoSortedLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2

        return dummy.next
        

# Testing
test1_vals1 = [1,2,4]
test1_vals2 = [1,3,4]
test1_expected = [1,1,2,3,4,4]

# Convert to list1 to LinkedList
test1_List1 = LinkedList()
test1_list1_node = ListNode(test1_vals1[0])
test1_List1.head = test1_list1_node
for val in test1_vals1[1:]:
    test1_list1_node.next = ListNode(val)
    test1_list1_node = test1_list1_node.next

# Convert to list2 to LinkedList
test1_List2 = LinkedList()
test1_list2_node = ListNode(test1_vals2[0])
test1_List2.head = test1_list2_node
for val in test1_vals2[1:]:
    test1_list2_node.next = ListNode(val)
    test1_list2_node = test1_list2_node.next

# Output of actual
solution_1 = Solution.MergeTwoSortedLists(test1_List1.head, test1_List2.head)
curr = solution_1
test1_actual = []

while curr:
    test1_actual.append(curr.val)
    curr = curr.next

# Compare expected with actual
assert len(test1_expected) == len(test1_actual), f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
for i in range(len(test1_expected)):
    assert(test1_expected[i] == test1_actual[i]), f"The actual result does not match all values for the expected result."
