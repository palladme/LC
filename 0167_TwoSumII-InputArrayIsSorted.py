# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

from typing import List
from collections import Counter


def TwoSumII_InputArrayIsSorted(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    current = numbers[l] + numbers[r]

    while l < r:
        while current < target:
            l += 1
            current = numbers[l] + numbers[r]
        while current > target:
            r -= 1
            current = numbers[l] + numbers[r]
        if current == target:
            return [l + 1,r + 1]
    
# Testing    
test1_numbers = [2,7,11,15]
test1_target = 9
test1_expected = [1,2]
test1_actual = TwoSumII_InputArrayIsSorted(test1_numbers,test1_target)

test2_numbers = [2,3,4]
test2_target = 6
test2_expected = [1,3]
test2_actual = TwoSumII_InputArrayIsSorted(test2_numbers, test2_target)

test3_numbers = [-1,0]
test3_target = -1
test3_expected = [1,2]
test3_actual = TwoSumII_InputArrayIsSorted(test3_numbers, test3_target)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is {test2_actual}."
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is {test3_actual}."
