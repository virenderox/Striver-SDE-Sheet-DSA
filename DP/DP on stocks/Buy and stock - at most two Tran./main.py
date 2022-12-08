class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[[-1 for _ in range(3)] for _ in range(3)] for _ in range(len(prices) + 1)]

        return self.solve(prices, 0 , True, 2,dp)

    def solve(self,prices, current, canBuy , transaction, dp):

        profit = 0
        #base case
        if current == len(prices) or transaction == 0:
            return 0

        if dp[current][canBuy][transaction] != -1:
            return dp[current][canBuy][transaction]

        if canBuy :

            profit =  max(-prices[current] + self.solve(prices,current + 1, False, transaction,dp), self.solve(prices,current + 1, True, transaction,dp))

        else:
            profit =  max(prices[current] + self.solve(prices,current + 1, True, transaction - 1,dp), self.solve(prices,current + 1, False, transaction,dp))

        dp[current][canBuy][transaction] = profit
        return profit

