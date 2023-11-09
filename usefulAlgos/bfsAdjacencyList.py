from collections import deque

def bfs(graph, start_vertices):
    visited = set()
    queue = deque(start_vertices)

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            # Process the current vertex here, e.g., print it
            print(vertex)

            # Add neighboring vertices to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
# Define your graph as a dictionary of adjacency lists
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Specify multiple starting vertices as a list
start_vertices = ['A', 'C', 'E']
bfs(graph, start_vertices)
