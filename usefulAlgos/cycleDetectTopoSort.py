from collections import defaultdict

def is_cyclic(graph):
    def has_cycle(vertex):
        visited.add(vertex)
        stack.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor in stack:
                return True  # Cycle detected

            if neighbor not in visited and has_cycle(neighbor):
                return True

        stack.remove(vertex)
        return False

    visited = set()
    stack = set()

    for vertex in graph:
        if vertex not in visited and has_cycle(vertex):
            return True  # Cycle detected

    return False  # No cycle detected

# Example usage:
# Define your directed graph as an adjacency list
graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E', 'A'],  # Introducing a cycle (D -> A)
    'E': []
}

graph_without_cycle = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

# Detect cycles in the graphs
has_cycle1 = is_cyclic(graph_with_cycle)
has_cycle2 = is_cyclic(graph_without_cycle)

# Print the results
print("Graph with cycle:", has_cycle1)
print("Graph without cycle:", has_cycle2)
