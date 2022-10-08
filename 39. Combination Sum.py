from typing import List
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = [] 
    lb = [] # list builder for generating valid lists. 
    def rec(i, t):
        # three base cases to deal with. 
        if t == 0: 
            res.append(lb.copy())
            return
        if t < 0 or i == len(candidates): 
            return 
        

        lb.append(candidates[i])
        # we include the current element and then keep adding the current element.
        rec(i, t - candidates[i])
        lb.pop()
        rec(i + 1, t)
    
    rec(0, target)
    return res
    

print(combinationSum([2,3,5], 8))