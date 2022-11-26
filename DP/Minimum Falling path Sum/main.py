class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = float("inf")
        for val_j in range(col):
            ans = min(ans,self.solve(matrix,0,val_j,row,col,{}))
        
        return ans


    def solve(self,matrix,current_i,current_j,row,col,dic):

        infy = float("inf")
        right_d = infy 
        left_d = infy 
        down = infy 

        if current_i == row - 1:
            return matrix[current_i][current_j]

        currentKey = (current_i, current_j)

        if currentKey in dic:
            return dic[currentKey]

        if current_j != 0:
            right_d = matrix[current_i][current_j] + self.solve(matrix,current_i + 1,current_j - 1,row , col,dic)
        
        down = matrix[current_i][current_j] + self.solve(matrix,current_i + 1,current_j, row,col,dic)

        if current_j != col-1:
            left_d = matrix[current_i][current_j] + self.solve(matrix,current_i + 1,current_j + 1, row,col,dic)

        dic[currentKey] = min(right_d, down, left_d)

        return dic[currentKey]
