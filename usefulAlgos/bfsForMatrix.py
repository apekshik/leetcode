from collections import deque

def bfs(matrix, starting_points):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    # this algorithm works with multiple start points for the traversal. 
    queue = deque(starting_points)

    while queue:
        x, y = queue.popleft()
        if (x, y) not in visited:
            visited.add((x, y))
            # Process the current cell here, e.g., print it
            print(matrix[x][y])

            # Define possible neighboring directions (up, down, left, right)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            # Add neighboring cells to the queue
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))

# Example usage:
# Define your 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Specify multiple starting points as a list of (x, y) coordinates
starting_points = [(0, 0), (1, 1), (2, 2)]

# Start BFS from all starting points simultaneously
bfs(matrix, starting_points)
