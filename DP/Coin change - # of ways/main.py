#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        
        dp = [[-1 for _ in range(Sum+1)] for _ in range(N + 1)]
        
        return self.solve(coins, N-1,Sum,dp)
        
    def solve(self,coins,current,target,dp):
        
        
        if target == 0:
            #print("in if")
            return 1
        if current == 0:
            #print("in second if")
            
            if target % coins[0] == 0:
                #print("in third if")
                return 1
                
            else:
                return 0
        
        if dp[current][target] != -1:
            return dp[current][target]
            
        notTaken = self.solve(coins,current-1,target,dp)
        taken = 0
        if target >= coins[current]:
            taken = self.solve(coins,current, target - coins[current], dp)
            
        dp[current][target] = taken + notTaken
            
        return dp[current][target]
        
        
        
        #base condition 
       # for i in range(N+1):
           # dp[i][0] = 1
        
        #for i in range(1,N+1):
            #for j in range(1,Sum + 1):
                
                #if j >= coins[i-1]:
                    
                    #dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                    
               # else:
                    #dp[i][j] = dp[i-1][j]
                    

        #return dp[N][Sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends
