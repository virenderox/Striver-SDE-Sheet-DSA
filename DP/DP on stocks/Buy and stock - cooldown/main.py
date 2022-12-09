#User function Template for python3

class Solution:
    def maximumProfit(self, prices, n):
        dp = [[0 for _ in range(3)] for _ in range(n + 2)]
        return self.solveTab(prices,n,dp)
        #return self.solve(prices,0,True, dp)
    def solveTab(self,prices,n,dp):
        
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j == 1:
                    dp[i][j] = max(-prices[i] + dp[i+1][0] , dp[i+1][1])
                else:
                    dp[i][j] = max(prices[i] + dp[i+2][1], dp[i+1][0])
                    
        return dp[0][1]

    def solve(self,prices,current,canBuy,dp):

        if current >= len(prices):
            return 0
        if dp[current][canBuy] != -1:
            return dp[current][canBuy]

        if canBuy:
            ideal = self.solve(prices, current + 1, canBuy,dp)
            buy = -prices[current] + self.solve(prices,current + 1, False,dp)
            dp[current][canBuy] = max(buy,ideal)
            return dp[current][canBuy]
        else:
            ideal = self.solve(prices,current + 1,canBuy,dp)
            sell = prices[current] + self.solve(prices,current + 2, True,dp)
            dp[current][canBuy] =  max(sell,ideal)
            return dp[current][canBuy]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        prices = list(map(int, input().split()))
        ob = Solution()
        print(ob.maximumProfit(prices, n))
# } Driver Code Ends
