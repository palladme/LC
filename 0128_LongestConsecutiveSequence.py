# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

from typing import List

def LongestConsecutiveSequence(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest
    
# Test 
test1_nums = [100,4,200,1,3,2]
test1_expected = 4
test1_actual = LongestConsecutiveSequence(test1_nums)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."

test2_nums = [0,3,7,2,5,8,4,6,0,1]
test2_expected = 9
test2_actual = LongestConsecutiveSequence(test2_nums)

assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."

