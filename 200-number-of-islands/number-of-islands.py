class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])

        def dfs(grid, x, y):
            if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != "1":
                return

            grid[x][y] = "$"
            dfs(grid, x + 1, y)
            dfs(grid, x - 1, y)
            dfs(grid, x, y + 1)
            dfs(grid, x, y - 1)

        island = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    island += 1

        return island
