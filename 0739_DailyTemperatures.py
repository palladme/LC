# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

from typing import List

def DailyTemperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    unused_temperatures = [] # stack of [index, temperature]

    for i, temperature in enumerate(temperatures):
        while unused_temperatures and temperature > unused_temperatures[-1][1]:
            stackI, stackT = unused_temperatures.pop()
            ans[stackI] = i - stackI
        unused_temperatures.append((i, temperature))
    return ans

# Testing
test1_temperatures = [73,74,75,71,69,72,76,73]
test1_expected = [1,1,4,2,1,1,0,0]
test1_actual = DailyTemperatures(test1_temperatures)

test2_temperatures = [30,40,50,60]
test2_expected = [1,1,1,0]
test2_actual = DailyTemperatures(test2_temperatures)

test3_temperatures = [30,60,90]
test3_expected = [1,1,0]
test3_actual = DailyTemperatures(test3_temperatures)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
