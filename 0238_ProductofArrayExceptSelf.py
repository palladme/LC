# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List

def ProductofArrayExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    for i in range(1, len(nums)):
        res[i] = nums[i-1] * res[i - 1]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = postfix * res[i]
        postfix *= nums[i]
    return res

test1_nums = [1,2,3,4]
test1_expected = [24,12,8,6]
test1_actual = ProductofArrayExceptSelf(test1_nums)

test2_nums = [-1,1,0,-3,3]
test2_expected = [0,0,9,0,0]
test2_actual = ProductofArrayExceptSelf(test2_nums)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}"
assert test2_actual == test2_actual, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}"




