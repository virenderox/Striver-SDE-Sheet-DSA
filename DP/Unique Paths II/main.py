class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1] == 1:
            return 0
        return self.solve(0,0,obstacleGrid, row,col,{})

    def solve(self,current_i,current_j,obstacleGrid,row,col,dic):

        if current_i== row-1 and current_j == col-1:
            return 1
        if current_i== row or current_j == col:
            return 0
        currentKey = (current_i,current_j)
        if currentKey in dic:
            return dic[currentKey]

        down = 0
        right = 0
        if obstacleGrid[current_i][current_j] != 1:

            down = self.solve(current_i + 1, current_j ,obstacleGrid,row,col,dic)
            right = self.solve(current_i , current_j + 1,obstacleGrid,row,col,dic)
            
        dic[currentKey] =  down + right
        return dic[currentKey]
