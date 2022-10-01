class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # the problem in leetcode just assumes the last step is one step higher than the given 
        # last element of the cost list. weird but yeah anyways, that's why we append the 0 there. 
        cost.append(0) 
        
        for i in range(len(cost) - 3, -1, -1): 
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])
    