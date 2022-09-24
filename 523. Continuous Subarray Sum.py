# this solution passed 92/96 test cases. 

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: 
            return False 
        
        # set to store previously discovered mod values. so they range from 0 to (k - 1) 
        s = set() 
        
        count = 0 
        s.add(0)
        pS = 0 
        for num in nums:
            # this if statement handles an annoying edge case of [1,0] k = 2 returns false and
            # [5, 0, 0, 0] k = 3 should return true. 
            if num == 0: 
                count += 1
                if count == 2: 
                    return True 
                continue 
            count = 0 
            # the actual algorithm. The idea is that basically while calculating the prefix sums as you 
            # iterate over the array, if the mod of that prefix sum was previously observed, we can return 
            # true since their difference would be divisible by the target k. Otherwise return false. 
            pS += num 
            if pS % k in s: 
                # if pS % k is already in s, we can return true because the difference would give us a number that is a multiple of k. 
                return True 
            else: 
                s.add(pS % k)
        
        return False 
                
''' Exactly same solution but also covers the edge cases by looking at the indices of the mod values we found 
as well. This is what I was also coming up in my head as a modification to the above code. The idea to use 
enumerations to get the index for the prefix sum is really good. Python allows you to do that. Interesting...

class Solution():
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {0:-1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False
'''