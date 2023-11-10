def dfs(matrix, start):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [start]

    # Define possible neighboring directions (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while stack:
        x, y = stack.pop()
        
        if not visited[x][y]:
            visited[x][y] = True
            # Process the current cell here, e.g., print it
            print(matrix[x][y])

            # Explore neighboring cells
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                    stack.append((new_x, new_y))

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Specify the starting cell as a tuple
start = (0, 0)

# Start iterative DFS from the specified cell
dfs(matrix, start)
