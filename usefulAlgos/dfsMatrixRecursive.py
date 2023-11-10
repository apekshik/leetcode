def dfs(matrix, start, visited):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])

    # Define possible neighboring directions (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    x, y = start

    # Mark the current cell as visited
    visited[x][y] = True

    # Process the current cell here, e.g., print it
    print(matrix[x][y])

    # Explore neighboring cells
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
            dfs(matrix, (new_x, new_y), visited)

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows, cols = len(matrix), len(matrix[0])
visited = [[False for _ in range(cols)] for _ in range(rows)]

# Specify the starting cell as a tuple
start = (0, 0)

# Start DFS from the specified cell
dfs(matrix, start, visited)
