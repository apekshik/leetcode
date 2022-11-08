def IncreasingLCS(L):
    n = len(L)
    LSort = L.sorted()
    mem = [[-1]*n]*n # creates a memoization table initialized with -1. 
    result = lcs(L, LSort, n, n, mem)
    return result

def lcs(X, Y, m, n, mem):
    if (mem[m - 1][n - 1] != -1):
        return mem[m - 1][n - 1]
    
    if (X[m - 1] == Y[n - 1]):
        mem[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1, mem)
        return mem[m - 1][n - 1]
    else:
        mem[m - 1][n - 1] = max(lcs(X, Y, m - 1, n, mem),
                                lcs(X, Y, m, n - 1, mem))
        return mem[m - 1][n - 1]



