# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11

from typing import List

def FindMinimumRotatedSortedArray(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    
    while l < r:
        m = l + (r - l)//2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m 
    return nums[l]

test1_nums = [3,4,5,1,2]
test1_expected = 1
test1_actual = FindMinimumRotatedSortedArray(test1_nums)
assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is {test1_actual}."

test2_nums = [3,4,5,1,2]
test2_expected = 1
test2_actual = FindMinimumRotatedSortedArray(test2_nums)
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is {test2_actual}."

test3_nums = [3,4,5,1,2]
test3_expected = 1
test3_actual = FindMinimumRotatedSortedArray(test3_nums)
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is {test3_actual}."
