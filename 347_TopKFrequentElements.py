# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    countMap = {}
    topfreq = [[] for n in range(len(nums) + 1)] 

    for num in nums:
        countMap[num] = countMap.get(num, 0) + 1

    for n, c in countMap.items():
        topfreq[c].append(n)
    
    topkfreq = []

    for i in range(len(topfreq) - 1 , 0, -1):
        for n in topfreq[i]:
            topkfreq.append(n)
            if len(topkfreq) == k:
                return topkfreq
    return topkfreq

#Test
test1_nums = [1,1,1,2,2,3]
test1_k = 2
test1_expected = [1,2]
test1_actual = topKFrequent(test1_nums, test1_k)

test2_nums = [1]
test2_k = 1
test2_expected = [1]
test2_actual = topKFrequent(test2_nums, test2_k)

assert test1_expected == test1_actual, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."
assert test2_expected == test2_actual, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."



