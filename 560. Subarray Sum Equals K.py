class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        m = [0]*len(nums) # calculate prefix sums in this array. 
        ps = {}  # save the counts of previous prefixSums in this map. 
        
        for i in range(1, len(nums)): 
            m[i] = nums[i] + m[i - 1]
            temp = m[i] - k 
            if temp in ps: 
                res += ps[m[i]] 
                
            if m[i] in ps: 
                ps[m[i]] += 1 
            else: 
                ps[m[i]] = 0 

            