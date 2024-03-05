# Example 1:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3

# Example 2:
# Input: target = 10, position = [3], speed = [3]
# Output: 1

# Example 3:
# Input: target = 100, position = [0,2,4], speed = [4,2,1]
# Output: 1

from typing import List

def CarFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [(p,s) for p,s in zip(position, speed)]
    pair.sort(reverse=True)
    time = []

    for p, s in pair:
        time.append((target - p) / s)
        while len(time) >= 2 and time[-1]<= time[-2]:
            time.pop()
    return len(time)  


test1_target = 12
test1_position = [10,8,0,5,3]
test1_speed = [2,4,1,1,3]
test1_expected = 3
test1_actual = CarFleet(test1_target, test1_position, test1_speed)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."

test2_target = 10
test2_position = [3]
test2_speed = [3]
test2_expected = 1
test2_actual = CarFleet(test2_target, test2_position, test2_speed)

assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."

test3_target = 100
test3_position = [0,2,4]
test3_speed = [4,2,1]
test3_expected = 1
test3_actual = CarFleet(test3_target, test3_position, test3_speed)

assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}."
