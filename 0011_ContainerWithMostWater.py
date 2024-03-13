# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Example 2:
# Input: height = [1,1]
# Output: 1

from typing import List

def ContainerWithMostWater(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    tallest = 0

    while l < r:
        if height[l] < height[r]:
            current = height[l] * (r - l)
            l += 1
        elif height[l] > height[r]:
            current = height[r] * (r - l)
            r -= 1
        else:
            current = height[l] * (r - l)
            l += 1
        tallest = max(tallest, current)

    return tallest

# Testing
test1_height = [1,8,6,2,5,4,8,3,7]
test1_expected = 49
test1_actual = ContainerWithMostWater(test1_height)

test2_height = [1,1]
test2_expected = 1
test2_actual = ContainerWithMostWater(test2_height)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
