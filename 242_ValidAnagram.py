# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Time: O(nlogn) , Space: O(1)
def ValidAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Time: O(n) , Space: O(1)
def ValidAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_arr = [0] * 26
    t_arr = [0] * 26
    for i in range(len(s)):
        s_arr[ord(s[i]) - ord('a')] += 1
        t_arr[ord(t[i]) - ord('a')] += 1
    return s_arr == t_arr

# Time: O(n) , Space: O(n)
def ValidAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Testing
test1_s = "rat"
test1_t = "car"
test1_expected = False
test1_actual = ValidAnagram(test1_s, test1_t)

test2_s = "rat"
test2_t = "tar"
test2_expected = True
test2_actual = ValidAnagram(test2_s, test2_t)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}"
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}"
