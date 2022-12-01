class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        return self.solve(grid,0,0,row,col,{})

    def solve(self,grid,current_i,current_j,row,col,dic):

        intMax = float("inf")
        if current_i == row - 1 and current_j == col - 1:
            return grid[row-1][col-1]

        if current_i == row or current_j == col:
            return intMax

        currentKey = (current_i, current_j)

        if currentKey in dic:
            return dic[currentKey]

        down = grid[current_i][current_j] + self.solve(grid,current_i + 1, current_j, row, col,dic)
        right = grid[current_i][current_j] + self.solve(grid,current_i , current_j + 1, row, col,dic)

        dic[currentKey] =  min(down,right)

        return dic[currentKey]
