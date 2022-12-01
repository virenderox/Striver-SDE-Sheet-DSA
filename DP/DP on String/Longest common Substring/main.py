#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2, n, m):
        
        if n == 0 or m == 0:
            return 0
            
        Max = -10000
            
        #intitialization and base condition included    
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        #filing up the table
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                #if charcheter matchs
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                #if we have discontinous
                else:
                    dp[i][j] = 0
                    
                    
                #Finding max value as longest can be in between string also
                Max = max(Max,dp[i][j])
                    
                    
        return Max
                
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends
