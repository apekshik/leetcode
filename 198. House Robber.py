
# brute force method involves making the decision of robbing the current house and skipping the next
# adjacent house, OR not robbing this house and robbing the next one. These are the two paths two take
# at any particular index of the array we're given. This gives us a 2^n time complexity solution. Surely
# time limit will exceed with this solution.  
class Solution2:
    def rob(self, nums: List[int]) -> int:
        def rec(A, i: int) -> int: 
            # leaf node where we've reached the end of the array. return 0. 
            if i >= len(A): 
                return 0
            
            # rob current house at i and skip adjacent house. 
            path1 = A[i] + rec(A, i + 2)
            # else don't rob current house and move to adjacent house.
            path2 = rec(A, i + 1) 
            # return max of the two paths. 
            return max(path1, path2) 
        
        return rec(nums, 0)

# Now, we use memoization to optimize the brute force approach.
# essentially, we figure out the max we can rob for each index i and store it 
# for later access. We can determine the max rob value of the next position by knowing the max 
# of the previous two positions. Let's say you have [...., rob1, rob2, n, n+1, ...]. To find the max
# rob value at index n, we just need max(rob1 + n, rob2). So, if we know rob1 and rob2 we can find n. 
# Then, we simply move to position n+1 with rob1 = rob2 and rob2 = n.  
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums: 
            temp = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2