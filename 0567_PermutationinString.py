# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

from typing import Counter

def PermutationinString(s1: str, s2: str) -> bool:
    counter = Counter(s1)
    s1_len = len(s1)

    for i in range(len(s2)):
        if s2[i] in counter:
            counter[s2[i]] -= 1
        
        if i > s1_len and s2[i - s1_len] in counter:
            counter[s2[i-s1_len]] += 1

        if all([counter[i] == 0 for i in counter]):
            return True       
    return False




# Testing

test1_s1 = "ab"
test1_s2 = "eidbaooo"
test1_expected = True
test1_actual = PermutationinString(test1_s1, test1_s2)

test2_s1 = "ab"
test2_s2 = "eidboaoo"
test2_expected = False
test2_actual = PermutationinString(test2_s1, test2_s2)

assert test1_actual == test1_expected,f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected,f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
