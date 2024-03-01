# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]

from typing import List

def _3Sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        l = i + 1
        r = len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while l < r:
            threesum = a + nums[l] + nums[r]

            if threesum < 0:
                l += 1
            elif threesum > 0:
                r -= 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

# Testing

test1_nums = [-1,0,1,2,-1,-4]
test1_expected = [[-1,-1,2],[-1,0,1]]
test1_actual = _3Sum(test1_nums)

test2_nums = [0,1,1]
test2_expected = []
test2_actual = _3Sum(test2_nums)

test3_nums = [0,0,0]
test3_expected = [[0,0,0]]
test3_actual = _3Sum(test3_nums)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is {test2_actual}."
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is {test3_actual}."

        

