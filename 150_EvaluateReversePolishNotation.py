# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9

# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6

# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
from typing import List

def EvaluateReversePolishNotation(tokens: List[str]) -> int:
    nums = []
    operators = {"+" : lambda x, y : int(x) + int(y),
                 "-" : lambda x, y : int(x) - int(y),
                 "*" : lambda x, y : int(x) * int(y),
                 "/" : lambda x, y : int(float(x) / float(y))}
    value = 0

    for token in tokens:
        if token[-1].isnumeric():
            nums.append(token)
        else:
            a = nums.pop()
            b = nums.pop()
            value = operators[token](b, a)
            nums.append(value)
    return value

# Testing       
test1_tokens = ["2","1","+","3","*"]
test1_expected = 9
test1_actual = EvaluateReversePolishNotation(test1_tokens)

test2_tokens = ["4","13","5","/","+"]
test2_expected = 6
test2_actual = EvaluateReversePolishNotation(test2_tokens)

test3_tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
test3_expected = 22
test3_actual = EvaluateReversePolishNotation(test3_tokens)  

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
