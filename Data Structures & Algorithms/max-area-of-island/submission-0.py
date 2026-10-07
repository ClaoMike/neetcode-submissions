from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()

        def getLandNeighbours(row, col):
            neighbours = []
            possible_neighbours = [ (row+1, col), (row-1, col), (row, col+1), (row, col-1) ]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]) and grid[n_row][n_col] == 1 and (n_row, n_col) not in seen:
                    neighbours.append( (n_row, n_col) )

            return neighbours
        
        def dfs(row, col):
            neighbours = getLandNeighbours(row, col)
            area = 1

            if not neighbours:
                return area

            for n_row, n_col in neighbours:
                if (n_row, n_col) not in seen:
                    seen.add( (n_row, n_col) )
                    area += dfs(n_row, n_col)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add( (i, j) )
                    max_area = max(max_area, dfs(i, j))

        return max_area