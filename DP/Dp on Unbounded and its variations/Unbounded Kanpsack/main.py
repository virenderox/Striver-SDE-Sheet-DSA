#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        
        #base condition already done
        dp = [[-1 for _ in range(W + 1)] for _ in range(N+1)]
        
        #Filling up the table
        #self.unboundedKnapSackTable(N,W,val,wt,dp)
        return self.unboundedKnapSackMemo(W,wt,val,N-1,dp)
        
    def unboundedKnapSackTable(self,N,W,val,wt,dp):
        
        for i in range(1,N+1):
            for j in range(1,W+1):
                
                if j >= wt[i-1]:
                    dp[i][j] = max(val[i-1] + dp[i][j - wt[i-1]] , dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                    
    def unboundedKnapSackMemo(self,W,wt,val,current,dp):
        
        if current == 0:
            return ((W//wt[0])) * val[0]
            
        #if current == 0 or W == 0:
            #return 0
        
        if dp[current][W] != -1:
            return dp[current][W]
            
        notTaken = 0 + self.unboundedKnapSackMemo(W,wt,val,current - 1, dp)
        
        taken = -100000
        if wt[current] <= W:
            taken = val[current] + self.unboundedKnapSackMemo(W - wt[current], wt,val,current,dp) 
            
        dp[current][W] = max(notTaken , taken)
        
        return dp[current][W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
