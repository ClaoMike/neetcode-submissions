from collections import defaultdict
from heapq import *
import math

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def getNeighbours(row, col):
            neighbours = []
            possible_neighbours = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[row]):
                    neighbours.append( (n_row, n_col) )
            
            return neighbours

        pq = []
        dist = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dist[(i, j)] = math.inf
        dist[(0, 0)] = grid[0][0]

        heappush(pq, (grid[0][0], (0, 0)))
        while pq:
            distance, (row, col) = heappop(pq)

            if distance > dist[(row, col)]:
                continue

            for n_row, n_col in getNeighbours(row, col):
                new_dist = max(distance, grid[n_row][n_col])
                
                if new_dist < dist[(n_row, n_col)]:
                    dist[(n_row, n_col)] = new_dist
                    heappush(pq, (new_dist, (n_row, n_col)))

        return dist[len(grid)-1, len(grid[0])-1]