from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if not nums:
            return 0

        nums = [-x for x in nums]

        heapq.heapify(nums)
        kth_distinct = 0

        while k > 0:
            k -= 1
            kth_distinct = -1 * heapq.heappop(nums)

        return kth_distinct
