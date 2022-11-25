class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        row = len(triangle)
        return self.solve(triangle,0,0,row, {})

    def solve(self,triangle,current_i,current_j,row,dic):

        if current_i == row-1:
            return triangle[current_i ][current_j]

        value = triangle[current_i][current_j]
        currentKey = (current_i, current_j)

        if currentKey in dic:
            return dic[currentKey]

        down =  value+ self.solve(triangle,current_i + 1, current_j,row,dic)
        right = value + self.solve(triangle,current_i + 1, current_j + 1,row,dic)

        dic[currentKey] = min(down,right)
        return dic[currentKey]

    
