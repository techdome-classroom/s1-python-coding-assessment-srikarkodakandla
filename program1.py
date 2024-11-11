class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            # Base case: if out of bounds or water, return
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 'W':
                return
            
            # Mark the current land cell as visited
            grid[i][j] = 'W'
            
            # Visit all 4 possible directions (up, down, left, right)
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left

        island_count = 0
        
        # Traverse the grid
        for i in range(rows):
            for j in range(cols):
                # If we find an unvisited land cell, it's the start of a new island
                if grid[i][j] == 'L':
                    island_count += 1
                    # Perform DFS to mark all connected land cells as visited
                    dfs(i, j)
        
        return island_count
