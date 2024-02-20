# Time: O(n), Space: O(n)
# len() is O(n) time
# set() is O(n) space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)        
        return len(hs) != len(nums)


# Time: O(n), Space: O(1)
# for loop is O(n)
# set() is O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False
