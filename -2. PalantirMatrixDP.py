
def solve(A): 
    n = len(A) # number of rows
    m = len(A[0]) # number of cols 
    # init B.
    B = [[0] * n for _ in range(m)]

    sum = 0
    # initialize rows
    for i in range(n):
        B[0][i] = sum + A[0][i]
        sum = B[0][i]

    # initialize cols 
    sum = 0 # reset to 0.
    for i in range(m): 
        B[i][0] = sum + A[i][0]
        sum = B[i][0]

    #    B[x][y] = B[x - 1][y] + B[x][y - 1] - B[x - 1][y - 1] + A[x][y]

    # fill the rest of the matrix B now
    for x in range(1, n):
        for y in range(1, m): 
            B[x][y] = B[x - 1][y] + B[x][y - 1] - B[x - 1][y - 1] + A[x][y]
     
    return B

    


A1 = [[1,2,3],[2,4,1],[5,1,2]]

print("Before")
for row in A1:
    print(row)

B1 = solve(A1)

print("After")
for row in B1: 
    print(row)