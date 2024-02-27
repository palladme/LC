# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List

def ContainsDuplicate(nums: List[int]) -> bool:
    dup_set = set()

    for num in nums:
        if num in dup_set:
            return True
        dup_set.add(num)
    return False

# Testing
test1_nums = [1,2,3,1]
test1_expected = True
test1_actual = ContainsDuplicate(test1_nums)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is {test1_actual}"

test2_nums = [1,2,3,4]
test2_expected = False
test2_actual = ContainsDuplicate(test2_nums)

assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is {test2_actual}"

test3_nums = [1,1,1,3,3,4,3,2,4,2]
test3_expected = True
test3_actual = ContainsDuplicate(test3_nums)

assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is {test3_actual}"
