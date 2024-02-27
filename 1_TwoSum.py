# Time = O(n); O(n) for looping the array, O(1) for using "in" operator, O(1) for inserting values into hashmap.
# Space = O(n) because Hashmap can get as large as the List.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm:
                return [hm.get(diff), i]
            hm[nums[i]] = i
        return []     
        
