from typing import List 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tb = [] # target builder. 
        visited = [False]*len(candidates)
        candidates.sort()
        def dfs(t, i):
            if t == 0:
                res.append(tb.copy())
            if t < 0: 
                return 

            prev = -1 
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                tb.append(candidates[j])
                dfs(t - candidates[j], j + 1)
                tb.pop()
                prev = candidates[j]

        dfs(target, 0)
        return res
        

S = Solution() 
print(S.combinationSum2([10,1,2,7,6,1,5], 8))
