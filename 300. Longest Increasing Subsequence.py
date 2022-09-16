res = []
sb = [] 
m = [0]
def rec(A, i): 
    if i >= len(A): 
        return 
    else: 
        if not sb or A[i] > sb[-1]:
            sb.append(A[i])
            print(sb)
            m[0] = max(m[0], len(sb))
            rec(A, i + 1)
            sb.pop() 
        
        rec(A, i + 1)

rec([0, 1, 0, 3, 2, 4], 0)
#print(sb)
print(sb)