import heapq 


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        # while the heapq has more than one element in it, keep doing  the following
        while len(stones) > 1: 
            #print(stones)
            # pop two of the largest stones out. 
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            # if equal then destroy them and continue
            if x == y: 
                continue
            # if not equal then find difference and push it back into the heap
            else: 
                heapq.heappush(stones, y - x)
        
        if len(stones) == 0: 
            return 0

        return -stones[0]

S = Solution 
print(S.lastStoneWeight(S, [2,7,4,1,8,1]))