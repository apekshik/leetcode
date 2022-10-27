from typing import List
import collections 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list (prerequisite Map) 
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # hashset to store visited nodes in the graph and cycle stores 
        # visited nodes in current dfs path to detect cycles. 
        visited, cycle = set(), set()
        res = [] # store final result in this to return in the end.
        def dfs(crs):
            # base case(s)
            if crs in cycle:
                return False
            # if crs visited do nothing. Just return True. 
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            # order of these three statements is very important. And that they come 
            # right after the dfs calls. 
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return res


s = Solution()

print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))