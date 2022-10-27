from typing import List

''' 
recursive greedy solution to activity selector (pg - 419, Thomas Cormen). 
'''
def actSelect(s: List[int], f: List[int], k: int, n: int) -> List[List[int]]:
    ''' 
    increasing order.  k is the iterator that represents the subset of S from k to end. 
    s and f are start and finish times of all activities. the activities were pre sorted in monotonically 
    n is the size of the whole activities array S. 
    '''
    m = k + 1 
    while m < n and s[m] <= f[k]:
        m += 1
    if m < n: 
        indices.append(m)
        return [test1[m]] + actSelect(s, f, m, n)
    return []



# test1 size = 12 
test1 = [[-2, 0], [1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], 
         [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]
        
# create s and f for the start and finish times. Note that the input list 
# should've been sorted prior to this with finish times in increasing order. 
s = [ test1[i][0] for i in range(len(test1)) ]
f = [ test1[i][1] for i in range(len(test1)) ]
indices = [] 

print(actSelect(s, f, 0, 12))
print(indices)



