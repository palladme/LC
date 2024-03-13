# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0

from typing import List

def BestTimetoBuyandSellStock(prices: List[int]) -> int:
    l = 0
    r = 1
    maxprofit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            maxprofit = max(maxprofit, prices[r] - prices[l]) 
            r += 1
        else:
            l = r
            r += 1
    return maxprofit

test1_prices = [7,1,5,3,6,4]
test1_expected = 5
test1_actual = BestTimetoBuyandSellStock(test1_prices)

test2_prices = [7,6,4,3,1]
test2_expected = 0
test2_actual = BestTimetoBuyandSellStock(test2_prices)

assert test1_actual == test1_expected, f"Test 1 should be {test1_expected} but is actually {test1_actual}."
assert test2_actual == test2_expected, f"Test 2 should be {test2_expected} but is actually {test2_actual}"
