from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        # If the starting color is already the target color, no changes needed
        if starting_color == color:
            return image

        # Get the image dimension
        m, n = len(image), len(image[0])

        # Define recursive DFS function
        def dfs(row: int, col: int):
            # Check if the current position is valid and has the original color
            if (0 <= row < m and 0 <= col < n and image[row][col] == starting_color):
                # Change the color
                image[row][col] = color

                # Recursively check the four adjacent cells
                dfs(row + 1, col) # Down
                dfs(row - 1, col) # Up
                dfs(row, col + 1) # Right
                dfs(row, col - 1) # Left

        # Start DFS from the given position
        dfs(sr, sc)
        return image

    # Alternative 1: Iterative DFS using a stack
    def floodFillIterativeDFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # If the starting color is already the target color, no changes needed
        if image[sr][sc] == color:
            return image

        # Get the original color and dimensions
        original_color = image[sr][sc]
        m,n = len(image), len(image[0])

        # Define the directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Use a stack for DFS
        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()

            # If current position is valid and has original color
            if 0 <= r < m and 0 <= c < n and image[r][c] == original_color:
                # Change the color
                image[r][c] = color

                # Add all four adjacent cells to the stack
                for dr, dc in directions:
                    stack.append((r + dr, c + dc))

        return image


    # Alternative 2: BFS using a queue
    def floodFillBFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # If the starting color is already the target color, no changes needed
        if image[sr][sc] == color:
            return image

        # Get the original color and dimensions
        original_color = image[sr][sc]
        m,n = len(image), len(image[0])

        # Define the directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Use a queue for BFS
        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()

            # If current position is valid and has the original color
            if 0 <= r < m and 0 <= c < n and image[r][c] == original_color:
                # Change the color
                image[r][c] = color

                # Add all four adjacent cells to the stack
                for dr, dc in directions:
                    queue.append((r + dr, c + dc))

        return image
