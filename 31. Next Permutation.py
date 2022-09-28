
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        we look at all subsequences of the input list from the end.
        we find the first minimum in the subsequence greater than the element to 
        the immediate right of the subsequence and swap with it. 
        Then we reverse the subsequence in place and we're done.  
        If we don't find one, we extend the subsequence by one to the right and look at the 
        next element and repeat. We terminate when the length of the subsequence becomes the 
        same as the lenght of the input list, in which case we reverse the whole list and 
        we're done. 
        '''
        
        # returns the index of the minimum in the sequence greater than the given arg.
        def min(x: int, beg) -> int: 
            if beg == len(nums) - 1: # we're looking at the last element of the list. 
                if nums[beg] > x: 
                    return beg 
                else: 
                    return None 

            for i in range(len(nums) - 1, beg, -1): 
                if nums[i] > x:
                    return i
            return None 

        def reverse(nums, beg: int): 
            for i in range(beg, len(nums) // 2): 
                print(nums[i])
                nums[i], nums[len(nums) - i] = nums[len(nums) - i], nums[i]

        e = len(nums) - 1
        while e > 0: 
            # print(nums[e])
            # print(nums[e - 1])
            minInd = min(nums[e - 1], e)
            # swap the min found with the value to the immediate right of the subsequnce. 
            # then reverse the subsequence in place and break out of the loop because we're done. 
            if minInd: 
                print(minInd)
                nums[e - 1], nums[minInd] = nums[minInd], nums[e - 1]
                print(e)
                reverse(nums, e)
                break 
            # else minimum found, expand the subsequence. 
            else: 
                e -= 1
                

T = Solution() 
A = [2,3,1,4,5]
B = [2,3,4,1,5]
C = [2,1,5,4,3]
# T.nextPermutation(C) 
# print(C)

def rev(nums, beg: int): 
    end = beg + (len(nums) - beg) // 2 + 1
    print(beg)
    print(end)

    for i in range(beg, end): 
        print(nums[len(nums) - i + 1])
        nums[i], nums[len(nums) - i] = nums[len(nums) - i], nums[i]
rev(A, 2)
print(A)

# rev(A, 1)
