class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 1
            
            if (r, c) in visit:
                return 0

            
            visit.add((r, c))
            count = dfs(r, c+1)
            count += dfs(r, c-1)
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)        
        