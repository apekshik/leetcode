
class Solution: 

    def riverSizes(self, mat) -> list:
        # result array that stores all river sizes.
        res = []
        # if mat size is 0, then bogus. 
        if len(mat) == 0: return []

        # iterate through mat and dfs into each new river. 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # if we encounter 0, ignore and move on.
                if mat[i][j] == 0:
                    continue 
                # if we encounter 1, dfs into the river. 
                if mat[i][j] == 1:
                    size = [1]
                    self.dfs(self, mat, i, j, size)
                    res.append(size[0])
                    # for line in mat:
                    #     for num in line: 
                    #         print(num, end= "\t")
                    #     print()
                    # print()

        
        return res

    def dfs(self, mat: list, i: int, j: int, size) -> int: 
        ''' we search for all parts of river and replace with them with -1. We also keep track of size of river.
        and pass it down the call stack to be updated by each recursive call into the river.'''
        mat[i][j] = -1
        # find the bounds of the matrix mat. 
        boundL = 0
        boundR = len(mat[0]) - 1
        bountT = 0
        boundB = len(mat) - 1

        if i + 1 <= boundB and mat[i + 1][j] == 1: 
            size[0] += 1
            self.dfs(self, mat, i + 1, j, size)
        if i - 1 >= 0 and mat[i][j] == 1:
            size[0] += 1
            self.dfs(self, mat, i - 1, j, size)
        if j - 1 >= 0 and mat[i][j - 1] == 1: 
            size[0] += 1
            self.dfs(self, mat, i, j - 1, size)
        if j + 1 <= boundR and mat[i][j + 1] == 1:
            size[0] += 1
            self.dfs(self, mat, i, j + 1, size)
        
        return

S = Solution 
mat = [
    [1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]
]

ans = {1, 4, 5, 6}
ans2 = S.riverSizes(S, mat)
print(ans == set(ans2))
print(ans2)