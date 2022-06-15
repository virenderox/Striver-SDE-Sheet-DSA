class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        r = [-1 for i in range(m)]
        c = [-1 for i in range(n)]
        #print(r,c)
        for row in range(m):
            for col in range(n):
                
                if matrix[row][col] == 0:
                    
                    r[row] = 0
                    c[col] = 0
                    
        #print(r,c)
                    
        for row in range(m):
            for col in range(n):
                
                if matrix[row][col] != 0:
                    
                    if r[row] == 0 or c[col] == 0:
                        matrix[row][col] = 0
                        
                    
                    
        
                        
                    
        
