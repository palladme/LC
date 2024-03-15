from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lengthpoint = []
        ans = []
        
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            
            lengthpoint.append([distance, point])
        
        heapq.heapify(lengthpoint)

        for i in range(k):
            temp = heapq.heappop(lengthpoint)
            ans.append(temp[1])
    
        return ans
