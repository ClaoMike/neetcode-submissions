from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_time = 0
        queue = deque()
        seen = set()
        count_fresh = 0
        count_rotten = 0
        total_fruits = 0

        def getFreshNeighbours(row, col):
            neighbours = []
            possible_neighbours = [ (row+1, col), (row-1, col), (row, col+1), (row, col-1) ]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]) and grid[n_row][n_col] == 1 and (n_row, n_col) not in seen:
                    neighbours.append( (n_row, n_col) )

            return neighbours

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append( ((i, j), 0) )
                    total_fruits += 1
                    count_rotten += 1
                elif grid[i][j] == 1:
                    total_fruits += 1
                    count_fresh += 1


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