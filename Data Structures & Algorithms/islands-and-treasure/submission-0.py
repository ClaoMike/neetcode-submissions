from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        seen = set()

        def getLandNeighbours(row, col):
            neighbours = []
            possible_neighbours = [ (row-1, col), (row+1, col), (row, col-1), (row, col+1) ]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]) and grid[n_row][n_col] != 0 and grid[n_row][n_col] != (-1) and (n_row, n_col) not in seen:
                    neighbours.append( (n_row, n_col) )

            return neighbours

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    seen.add( (i, j) )
                    queue.append( ((i, j), 0) )

        while queue:
            (row, col), distance = queue.popleft()

            neighbours = getLandNeighbours(row, col)

            for n_row, n_col in neighbours:
                grid[n_row][n_col] = distance + 1

                seen.add( (n_row, n_col) )
                queue.append( ((n_row, n_col), distance + 1) )