def getMostVisited(n, sprints):
    # Write your code here
    visits = dict.fromkeys(range(1, n + 1), 0)

    for i in range(len(sprints) - 1): # we only go till the second last element. 
        if sprints[i] < sprints[i + 1]:
            # normal do normal shit.
            l = sprints[i]
            r = sprints[i + 1]
        else: 
            # revers range and update the dict. 
            l = sprints[i + 1]
            r = sprints[i]
    
        for j in range(l, r + 1): 
            visits[j] += 1

    m, res = 0, 1
    for i in range(len(visits)):
        if m < visits[i + 1]:
            m = visits[i + 1]
            res = i + 1
    
    return res 


print(getMostVisited(5, [2, 4, 1, 3]))
print(getMostVisited(10, [1, 5, 10, 3]))
print(getMostVisited(5, [1,5]))
print(getMostVisited(9, [9, 7, 3, 1] ))