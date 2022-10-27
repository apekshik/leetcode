from typing import List 
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a prerequisite Map (essentially an adjacency list)
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)
            
        # set of nodes visited in current dfs path. 
        visited = set()
        def dfs(crs):
            ## two base cases. 
            # loop detected if the course is already in the visited set.
            if crs in visited: 
                return False
            # if the course has no prerequisites, return True. 
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for nextCrs in preMap[crs]:
                if not dfs(nextCrs): return False
            visited.remove(crs)
            ''' genius move to reset preMap[crs] to empty. It means we visited this path already
             and the next time we reach this course path we don't need to go down it 
             further because the second base case will return true since the for loop 
             above didn't detect a cycle down this course path. '''
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            # if dfs returns false, found loop, so return false. 
            if not dfs(crs): return False
        
        return True