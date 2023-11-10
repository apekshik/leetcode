import heapq

def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity, except for the start vertex as 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Create a priority queue to store vertices and their distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if the current distance is greater than the recorded distance
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
# Define your graph as an adjacency list with weighted edges
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 7},
    'C': {'A': 4, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 7, 'F': 3},
    'F': {'C': 5, 'E': 3}
}

# Specify the starting vertex
start_vertex = 'A'

# Find the shortest distances from the starting vertex
shortest_distances = dijkstra(graph, start_vertex)

# Print the shortest distances to each vertex
for vertex, distance in shortest_distances.items():
    print(f'Shortest distance from {start_vertex} to {vertex}: {distance}')
