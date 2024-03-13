# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from typing import List
from collections import defaultdict

def GroupAnagrams(strs: List[str]) -> List[List[str]]:
    ana_map = defaultdict(list)

    for s in strs:
        ch_arr = [0] * 26
        for c in s:
            ch_arr[ord(c) - ord('a')] += 1
        ana_map[tuple(ch_arr)].append(s)
    
    return ana_map.values()

# testing
test1_strs = ["eat","tea","tan","ate","nat","bat"]
test1_expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
test1_actual = GroupAnagrams(test1_strs)

assert test1_strs.sort() == test1_expected.sort(), f"Test 1 is expected to output {test1_expected} but outputeed {test1_actual}"

