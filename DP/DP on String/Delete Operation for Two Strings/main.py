class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        lenLCS = self.Lcs(word1,word2,m,n)
        op1  = m - lenLCS
        op2 =  n - lenLCS
        return op1 + op2
         
    def Lcs(self,x,y,n,m):
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[n][m]
