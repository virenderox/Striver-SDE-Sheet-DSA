#User function Template for python3

class Solution:
    def countWays(self, N, S):
        
        if N == 1:
            if S[0] == 'T':
                return 1
            else:
                return 0
        
        dp = [[[-1 for i in range(2)] for i in range(N + 1)] for j in range(N + 1)]
        return self.solve(S,0,N-1,1,dp)
        
    def solve(self,S,i,j,isTrue,dp):
        
        mod = 1003
        
        #base cases
        #if we shrink our index
        if i > j:
            return 0
        #if only single element present    
        if i == j:
            if isTrue == True:
                return S[i] == 'T'
            else:
                return S[i] == 'F'
                
        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]
                
        #we are K-loop
        ans = 0
        for k in range(i+1,j,2):
        
            
            left_t = self.solve(S,i,k-1,1,dp)
            left_f = self.solve(S,i,k-1,0,dp)
            
            right_t = self.solve(S,k+1,j,1,dp)
            right_f = self.solve(S,k+1,j,0,dp)
            
            if S[k] == '&':
                
                if isTrue == True:
                    ans = (ans + (left_t * right_t)%mod)%mod
                else:
                    ans = (ans + (left_t * right_f)%mod + (left_f * right_t)%mod + (left_f * right_f)%mod)%mod
                    
            elif S[k] == '|':
                if isTrue == True:
                    ans = (ans + (left_f * right_t)%mod + (left_t * right_f)%mod + (left_t * right_t)%mod)%mod
                else:
                    ans =  (ans + (left_f * right_f)%mod)%mod
                    
            elif S[k] == '^':
                if isTrue == True:
                    ans = (ans + (left_f * right_t)%mod + (left_t * right_f)%mod)%mod
                else:
                    ans =  (ans + (left_t * right_t)%mod + (left_f * right_f)%mod)%mod
                    
            dp[i][j][isTrue] = ans 
            
        return dp[i][j][isTrue]
                   
                    
                
            
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends
