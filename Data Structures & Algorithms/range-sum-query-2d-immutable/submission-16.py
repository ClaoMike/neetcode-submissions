class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = [[matrix[0][0]]]

        for i in range(1, len(matrix[0])):
            prefix[0].append(prefix[0][-1] + matrix[0][i])

        for i in range(1, len(matrix)):
            prefix.append([])

        for i in range(1, len(matrix)):
            prefix[i].append(prefix[i-1][0] + matrix[i][0])
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                prefix[i].append( matrix[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] )

        self.prefix = prefix
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 or col1 == 0:
            behind = 0
        else:
            behind = self.prefix[row1-1][col1-1]

        if col1 == 0:
            left = 0
        else:
            left = self.prefix[row2][col1-1]
        
        if row1 == 0:
            top = 0
        else:
            top = self.prefix[row1-1][col2]

        return self.prefix[row2][col2] - top - left + behind


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)