# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: s = "race a car"
# Output: false

# Example 3:
# Input: s = " "
# Output: true

def ValidPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        while not isalphanum(s[i]) and i < j:
            i += 1
        
        while not isalphanum(s[j]) and i < j:
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True 

def isalphanum(w: str) -> bool:
    return w.isalpha() or w.isnumeric()


test1_s = "A man, a plan, a canal: Panama"
test1_expected = True
test1_actual = ValidPalindrome(test1_s)

test2_s = "race a car"
test2_expected = False
test2_actual = ValidPalindrome(test2_s)

test3_s = " "
test3_expected = True
test3_actual = ValidPalindrome(test3_s)

assert test1_expected == test1_actual, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_expected == test2_actual, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
assert test3_expected == test3_actual, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
