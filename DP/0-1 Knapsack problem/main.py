#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        dp = [[-1 for i in range(W+1)] for j in range(n+1)]
        return self.solve(W,wt,val,n-1, dp)
        
    def solve(self,W,wt,val,current,dp):
        
        if current < 0:
            return 0
        
        if dp[current][W] != -1:
            return dp[current][W]
            
        notTaken = self.solve(W,wt,val,current - 1,dp)
        
        taken = float('-inf')
        
        if wt[current] <= W:
            taken = self.solve(W - wt[current], wt, val, current - 1,dp) + val[current]
         
        dp[current][W] = max(taken,notTaken)  
        return dp[current][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
