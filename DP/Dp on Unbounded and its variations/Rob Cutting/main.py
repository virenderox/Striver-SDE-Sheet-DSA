#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        lenth =[]
        for i in range(1,n+1):
            lenth.append(i)
            
        dp = [[-1 for _ in range(n + 1)] for _ in range(n+1)] 
        return self.unboundedKnapSackMemo(n-1,n,price,lenth,dp)
        #return dp[n][n]
            
    def unboundedKnapSackTable(self,N,W,val,wt,dp):
        
        for i in range(1,N+1):
            for j in range(1,W+1):
                
                if j >= wt[i-1]:
                    dp[i][j] = max(val[i-1] + dp[i][j - wt[i-1]] , dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
            
            
    def unboundedKnapSackMemo(self,current,W,val,wt,dp):
        
        if current == 0:
            return ((W//wt[0])) * val[0]
            
        #if current == 0 or W == 0:
            #return 0
        
        if dp[current][W] != -1:
            return dp[current][W]
            
        notTaken = 0 + self.unboundedKnapSackMemo(current - 1,W,val,wt, dp)
        
        taken = -100000
        if wt[current] <= W:
            taken = val[current] + self.unboundedKnapSackMemo(current,W - wt[current],val,wt,dp) 
            
        dp[current][W] = max(notTaken , taken)
        
        return dp[current][W]
        
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
