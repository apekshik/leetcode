import heapq


def minCostConPoints(points) -> int: # points is a list of lists 
    N = len(points)
    ''' we don't store the points themselves in the hashmap because lists aren't hashable 
    # in python and we assign the points indices from 0 to N - 1 instead. '''
    adj = { i:[] for i in range(N) } # i : list of adjacent nodes in the spanning tree. 

    ''' we also don't directly store the adjacent points themselves for each point in the 
    # hasmap. We calculate the distance to every other point connected and store the index
    # to that point in the list. We're essentially doing some of the work of calculating 
    # the distance as we're building our adjacency list here. '''
    for i in range(N): 
        x1, y1 = points[i]
        ''' inner for loop only needs to go from i + 1 to the N - 1 because at each step
        # we're connecting both ways in each iteration (since it's just a regular graph) '''
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2) 
            adj[i].append([dist, j]) 
            adj[j].append([dist, i]) 

    ''' Finally, we basically implement the Prim's Algorithm for Min spanning trees with 
    O(n^2lg(n)) complexity. We use a hashset to keep track of previously visited nodes,
    a min heap to store the min distance for each of the nodes (nlg(n)) time complexity comes 
    from here) and then we pop the min distance each time for each node (so that's n times nlog(n)).
    The space complexity is well linear since we used three linear data structures to solve this.'''

    res = 0 
    vis = set()
    minH = [[0,0]]
    while len(vis) < N:
        cost, i = heapq.heappop(minH)
        if i in vis: # don't understand why we do this. 
            continue
        res += cost 
        vis.add(i)
        for neiCost, nei in adj[i]:
            if nei not in vis: # to make sure we don't add previously visited neighbors 
                heapq.heappush(minH, [neiCost, nei]) 

    return res    


p1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]

print(minCostConPoints(p1))