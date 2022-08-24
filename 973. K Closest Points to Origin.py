import math 
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        # distances = []
        # for point in points: 
        #     distance = math.sqrt(point[0]**2 + point[1]**2)
        #     distances.append([distance, point])
        # The above code written in one line. 
        distances = [(math.sqrt(point[0]**2 + point[1]**2), point) for point in points]

        heapq.heapify(distances) # heap with key as the distance. 

        for i in range(k): 
            res.append(heapq.heappop(distances)[1])

        return res 