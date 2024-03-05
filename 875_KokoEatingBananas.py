# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

import math
from typing import List

def KokoEatingBananas(piles: List[int], h: int) ->  int:
    l = 1
    r = max(piles)
    ans = r

    while l <= r:
        m = l + (r-l)//2
        hours = 0

        for pile in piles:
            hours += math.ceil(pile/m)
    
        if hours <= h:
            ans = min(ans,m) 
            r = m - 1
        else:
            l = m + 1
    return ans

# Testing
test1_piles = [3,6,7,11]
test1_h = 8
test1_expected = 4
test1_actual = KokoEatingBananas(test1_piles, test1_h)
assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}"

test2_piles = [30,11,23,4,20]
test2_h = 5
test2_expected = 30
test2_actual = KokoEatingBananas(test2_piles, test2_h)
assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}"

test3_piles = [30,11,23,4,20]
test3_h = 6
test3_expected = 23
test3_actual = KokoEatingBananas(test3_piles, test3_h)
assert test3_actual == test3_expected, f"Test 3 is expected to be {test3_expected} but is actually {test3_actual}"
