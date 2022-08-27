# simply a genius solution. One could've used two separate arrays to store the prefix and postfix
# products and then use them in conjunction to find the res[] array. However, that takes O(n) time and space. 
# the following solution does the same thing only using the res[] array (in place basically) so it takes O(n) 
# time but O(1) space. 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        # the prefix calculation is pretty obvious. 
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
