# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

def ValidParentheses(s: str) -> bool:
    hm = { ")" : "(", 
          "]" : "[", 
          "}" : "{"}
    
    current = []

    for c in s:
        if c in hm and current:
            if current.pop() != hm[c]:
                return False
        else:
            current.append(c)
    return True if len(current) == 0 else False

# Testing
test1_s = "()"
test1_expected = True
test1_actual = ValidParentheses(test1_s)

test2_s = "()[]{}"
test2_expected = True
test2_actual = ValidParentheses(test2_s)

test3_s = "(]"
test3_expected = False
test3_actual = ValidParentheses(test3_s)


assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
    
    
