from collections import defaultdict

def topological_sort(graph):
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)

    visited = set()
    stack = []
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  # Reverse the result to get the topological order

# Example usage:
# Define your directed acyclic graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}

# Perform topological sorting
topological_order = topological_sort(graph)

# Print the topological order
print(topological_order)
