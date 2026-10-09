from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        zeros = set()
        queue = deque()

        def getNeighbours(row, col):
            neighbours = []
            possible_neighbours = [ (row-1, col), (row+1, col), (row, col-1), (row, col+1) ]
            for n_row, n_col in possible_neighbours:
                if 0 <= n_row < len(board) and 0 <= n_col < len(board[n_row]) and board[n_row][n_col] == "O" and (n_row, n_col) not in seen:
                    neighbours.append( (n_row, n_col) )

            return neighbours
        
        def onTheBorder(row, col):
            return ( row == 0 or row == len(board)-1 or col == 0 or col == len(board[row])-1 )

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    zeros.add( (i, j) )
                    if onTheBorder(i, j):
                        seen.add( (i, j) )
                        queue.append( (i, j) )

        while queue:
            row, col = queue.popleft()

            for n_row, n_col in getNeighbours(row, col):
                seen.add( (n_row, n_col) )
                queue.append( (n_row, n_col) )

        for row, col in zeros.difference(seen):
            board[row][col] = "X"