# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4

def LongestRepeatingCharacterReplacement(s: str, k: int) -> int:
    count = {}
    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
    
    return (r - l + 1)

# Testing

test1_s = "ABAB"
test1_k = 2
test1_expected = 4
test1_actual = LongestRepeatingCharacterReplacement(test1_s, test1_k)


test2_s = "AABABBA"
test2_k = 1
test2_expected = 4
test2_actual = LongestRepeatingCharacterReplacement(test2_s, test2_k)


assert test1_actual == test1_expected,f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected,f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
