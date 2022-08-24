# You must solve it in O(n) time complexity. 
# So we use the quickSelect approach. 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            # pivot is what we compare the value at index i. The pivot  
            # partitions the array into two (hopefully) equal halves. 
            pivot, p = nums[r], l 

            for i in range(l, r):
                if nums[i] < pivot:
                    # swapping in python can be done like this. 
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1 # incremement p to know how many numbers were below pivots value. 
            nums[r], nums[p] = nums[p], nums[r] # swap the value of pivot with the value at index p.

            if k < p:  return quickSelect(l, p - 1)
            elif k > p:return quickSelect(p + 1, r)
            else:      return nums[k]

        return quickSelect(0, len(nums) - 1)