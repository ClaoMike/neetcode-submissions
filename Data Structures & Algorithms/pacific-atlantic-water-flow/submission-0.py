from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic, seen = set(), set(), set()
        queue = deque()

        def getValidNeighbours(row, col):
            neighbours = []
            possible_neighbours = [ (row+1, col), (row-1, col), (row, col+1), (row, col-1) ]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(heights) and 0 <= n_col < len(heights[n_row]) and heights[n_row][n_col] >= heights[row][col] and (n_row, n_col) not in seen:
                    neighbours.append( (n_row, n_col) )
            return neighbours

        def proccessNode(i, j):
            seen.add( (i, j) )
            queue.append( (i, j) )

        def bfs(ocean):
            while queue:
                row, col = queue.popleft()
                ocean.add( (row, col) )

                for n_row, n_col in getValidNeighbours(row, col):
                    proccessNode(n_row, n_col)

        def appendRowToQueue(i):
            for j in range(len(heights[i])):
                proccessNode(i, j)

        appendRowToQueue(0) 
        
        j = 0
        for i in range(1, len(heights)):
            proccessNode(i, j)

        bfs(pacific)

        seen.clear()
        queue.clear()
        
        appendRowToQueue(len(heights)-1) 
        
        j = len(heights[0])-1
        for i in range(len(heights)-1):
            proccessNode(i, j)

        bfs(atlantic)

        return list(pacific.intersection(atlantic))