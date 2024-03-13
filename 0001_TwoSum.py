# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List

def TwoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in num_map:
            return [i, num_map[diff]]
        
        num_map[n] = i

# Testing
test1_nums = [2,7,11,15]
test1_target = 9
test1_expected = [0,1]
test1_expected1 = [1,0]
test1_actual = TwoSum(test1_nums, test1_target)
assert test1_actual == test1_expected or test1_expected1, f"Test 1 is expected to be {test1_expected} but is {test1_actual}"


