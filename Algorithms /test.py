import collections
from typing import List
# example Facts
eF = [
    ["m", 3.28, "ft"],
    ["ft", 12, "in"],
    ["hr", 60, "min"],
    ['min', 60, 'sec'],
]

# example queries
eQ = [
    [2, "m", "in"], # 2 m = ? in -> answer = 78.82
    [13, "in", "m"], # 13 in = ? m -> answer = 0.330
    [13, "in", "hr"], # not convertible!
] 

# we take facts and convert it to a graph since we want bidirectional unit conversion.

def createGraph(facts) -> dict:
    adj = collections.defaultdict(list)
    for u, c, v in facts:
        adj[u].append((v, c))
        adj[v].append((u, 1 / c))
    return adj


''' we then take the graph and process queries with it. We create a function that takes a query,
takes a graph (in the form of an adjacency list) and hopefully prints out the converted value 
if it's possible to convert it to said unit.'''
def handleQueryDFS(query: list, adj: dict):
    ''' query is a list of (float, str, str) with '''
    val, start, final = query
    res = [val]
    visited = set()
    convShortcut = [1]
    def dfs(unit):
        visited.add(unit)
        for adjUnit, convertRatio in adj[unit]:
            if adjUnit in visited:
                continue
            if final == adjUnit: # we've found the final conversion unit. 
                res[0] *= convertRatio
                # add convertShortcut edge to graph.
                convShortcut[0] *= convertRatio
                adj[start].append((final, convShortcut[0]))
                adj[final].append((start, 1 / convShortcut[0]))
                return True
            res[0] *= convertRatio
            convShortcut[0] *= convertRatio
            if dfs(adjUnit): return True
            res[0] /= convertRatio
            convShortcut[0] /= convertRatio
        return False

    if dfs(start): 
        return res[0]
    else: 
        return "Not convertible!"

print(handleQueryDFS(eQ[0], createGraph(eF)))

def handleQueryBFS(query: list, adj: dict):
    return None