#User function Template for python3

class Solution:
    def maximumProfit(self, prices, n, fee):
        dp = [[0 for _ in range(3)] for _ in range(n + 2)]
        return self.solveTab(prices,n,dp,fee)
        #return self.solve(prices,0,True, dp)
    def solveTab(self,prices,n,dp,fee):
        
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j == 1:
                    dp[i][j] = max(-prices[i] + dp[i+1][0] , dp[i+1][1])
                else:
                    dp[i][j] = max(prices[i] + dp[i+1][1] - fee, dp[i+1][0]) 
                    
        return dp[0][1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        prices = list(map(int, input().split()))
        fee=int(input())
        ob = Solution()
        print(ob.maximumProfit(prices, n, fee))
# } Driver Code Ends


-----------------------------------------------------------------------------------------------------------------


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        dp = [[-1 for _ in range(3)] for _ in range(len(prices) + 1)]
        return self.solve(prices,0,True, dp, fee)

    def solve(self,prices,current,canBuy,dp,fee):

        if current >= len(prices):
            return 0
        if dp[current][canBuy] != -1:
            return dp[current][canBuy]

        if canBuy:
            ideal = self.solve(prices, current + 1, canBuy,dp,fee)
            buy = -prices[current] + self.solve(prices,current + 1, False,dp,fee)
            dp[current][canBuy] = max(buy,ideal)
            return dp[current][canBuy]
        else:
            ideal = self.solve(prices,current + 1,canBuy,dp,fee)
            sell = prices[current] + self.solve(prices,current + 1, True,dp,fee) - fee
            dp[current][canBuy] =  max(sell,ideal)
            return dp[current][canBuy]
