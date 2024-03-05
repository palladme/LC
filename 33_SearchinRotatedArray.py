# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

from typing import List

def SearchinRotatedArray(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + (r-1)//2

        if target == nums[m]:
            return m

        if nums[l] < nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1

        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1

# Testing
test1_nums = [4,5,6,7,0,1,2]
test1_target = 0
test1_expected = 4
test1_actual = SearchinRotatedArray(test1_nums, test1_target)
assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."

test2_nums = [4,5,6,7,0,1,2]
test2_target = 0
test2_expected = 4
test2_actual = SearchinRotatedArray(test2_nums, test2_target)
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."

test3_nums = [4,5,6,7,0,1,2]
test3_target = 0
test3_expected = 4
test3_actual = SearchinRotatedArray(test3_nums, test3_target)
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
