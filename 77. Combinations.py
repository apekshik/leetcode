def comb(n, k): # returns a list of lists.
    res = [] 
    lb  = [] # build each list that gets added to the list. 
    def help(i):
        # base cases.  
        if len(lb) == k:
            res.append(lb.copy())
            return 
        if i == n + 1:
            return 
        
        lb.append(i)
        help(i + 1) # recursion path including current number
        lb.pop() # backtrack step 
        help(i + 1) # recursion path excluding current number

    help(1)
    return res 

print(comb(5, 2))

b = []
r = []
def rec(i, k):
    if len(b) == k: 
        r.append(b.copy())
        return 
    if i == 6:
        return
    b.append(i)
    rec(i + 1, k) 
    b.pop()
    rec(i + 1, k)

rec(1, 4)
# print(r)