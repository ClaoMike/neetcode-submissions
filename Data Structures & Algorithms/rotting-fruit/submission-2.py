from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_time, count_rotten, total_fruits = 0, 0, 0
        queue = deque()
        seen = set()

        def getFreshNeighbours(row, col):
            neighbours = []
            possible_neighbours = [ (row+1, col), (row-1, col), (row, col+1), (row, col-1) ]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]) and grid[n_row][n_col] == 1 and (n_row, n_col) not in seen:
                    neighbours.append( (n_row, n_col) )

            return neighbours

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    total_fruits += 1
                
                if grid[i][j] == 2:
                    queue.append( ((i, j), 0) )
                    count_rotten += 1

        while queue:
            (row, col), minutes = queue.popleft()
            total_time = max(total_time, minutes)

            for n_row, n_col in getFreshNeighbours(row, col):
                count_rotten += 1
                seen.add( (n_row, n_col) )
                queue.append( ((n_row, n_col), minutes+1) )

        if total_fruits != count_rotten:
            return -1

        return total_time