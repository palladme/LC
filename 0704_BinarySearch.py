# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4


# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1

from typing import List

def BinarySearch(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        m = l + (r - l)// 2  

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1

test1_nums = [-1,0,3,5,9,12]
test1_target = 9
test1_expected = 4
test1_actual = BinarySearch(test1_nums, test1_target)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is {test1_actual}."
