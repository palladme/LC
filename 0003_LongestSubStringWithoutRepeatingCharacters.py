# Example 1:
# Input: s = "abcabcbb"
# Output: 3

# Example 2:
# Input: s = "bbbbb"
# Output: 1

# Example 3:
# Input: s = "pwwkew"
# Output: 3

def LongestSubStringWithoutRepeatingCharacters(s: str) -> int:
    hs = set()
    l = 0
    longest = 0

    for r in range(len(s)):
        while s[r] in hs:
            hs.remove(s[l])
            l += 1 
        hs.add(s[r])
        longest = max(longest, r - l + 1)
    return longest

# Testing

test1_s = "abcabcbb"
test1_expected = 3
test1_actual = LongestSubStringWithoutRepeatingCharacters(test1_s)

test2_s = "bbbbb"
test2_expected = 1
test2_actual = LongestSubStringWithoutRepeatingCharacters(test2_s)

test3_s = "pwwkew"
test3_expected = 3
test3_actual = LongestSubStringWithoutRepeatingCharacters(test3_s)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."





