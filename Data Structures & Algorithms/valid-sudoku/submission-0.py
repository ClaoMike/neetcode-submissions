class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        for row in board:
            c = Counter(row)
            for key, value in c.items():
                if key != "." and value > 1:
                    return False 

        for col in zip(*board):
            c = Counter(col)
            for key, value in c.items():
                if key != "." and value > 1:
                    return False 

        i = 0
        while i < 9:
            col = 0
            while col < 9:
                submatrix = [row[col:col+3] for row in board[i: i+3] ]
                c = Counter()
                for row in submatrix:
                    c += Counter(row)
                for key, value in c.items():
                    if key != "." and value > 1:
                        return False 
                col += 3
            i += 3


        return True