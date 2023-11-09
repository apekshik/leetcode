from typing import List 
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        for row in grid: 
            print(row)

        # Do a BFS since the rotting algorithm moves in waves through our gird of oranges. We need to keep track of visited oranges. Also, we need to know the location of all rotten oranges to begin with (this already caps the lower bound at O(mn)).
        
        # find all rotting oranges and store indices
        rotInd = [] 
        # We have fresh count so that we decrement it when going through the rotting process. 
        # If freshCnt is more than 0 after BFS traversal some of the oranges aren't reachable.
        freshCnt = 0
        for i in range(len(grid)): 
            for j in range(len(row)): 
                if grid[i][j] == 2: 
                    rotInd.append((i, j))
                if grid[i][j] == 1: 
                    freshCnt = freshCnt + 1 


        if freshCnt == 0: 
            return 0
        
        # Define possible neighboring directions (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(mat, startVertices, freshCnt): 
            totalTime = 0
            vis = set()
            rows, cols = len(mat), len(mat[0])
            # initialize queue with start vertices. 
            q = deque(startVertices) 
            while q:
                print("The queue currently looks like: ", q)
                for row in mat: 
                    print(row)

                # make copy so the number of iterations is fixed. 
                newQ = q.copy()
                for _ in newQ: 
                    x, y = q.popleft()
                    vis.add((x, y))
                    # add neighbours to the queue if they're not rotten. 
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy # calculate the new x and y indices.
                        if 0 <= nx < rows and 0 <= ny < cols and (mat[nx][ny] == 1) and (nx, ny) not in vis:
                            mat[nx][ny] = 2
                            freshCnt = freshCnt - 1
                            q.append((nx, ny))

                
                totalTime = totalTime + 1 

            print("Fresh count:", freshCnt)
            if freshCnt > 0: 
                return -1
            return totalTime 
        return bfs(grid, rotInd, freshCnt=freshCnt)

S = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]] 
grid2 = [[1,2,1,0],[0,1,0,1],[1,1,0,0],[1,0,0,1]]
print(S.orangesRotting(grid2))
