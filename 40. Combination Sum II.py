from typing import List 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        tb = set() # target builder. 
        visited = [False]*len(candidates)
        
        def dfs(t, i):
            if t == 0 and tb not in res: 
                res.add(tb.copy())
                return 
            
            for j in range(len(candidates)):
                if j == i or visited[j] == True:
                    continue
                if candidates[j] <= t: 
                    visited[j] = True 
                    tb.add(candidates[j])
                    dfs(t - candidates[j], j)
                    # backtrack.
                    visited[j] = False  
                    tb.remove(candidates[j])
        
        dfs(target, 0)
        
        

S = Solution() 
print(S.combinationSum2([10,1,2,7,6,1,5], 8))
