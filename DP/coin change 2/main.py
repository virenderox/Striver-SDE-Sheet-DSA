class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        Inf = float('inf')
        dp = [[-1 for i in range(amount + 1)] for j in range(n+1)]

        value = self.solve(coins,n-1,amount,dp)
        if value == inf:
            return -1
        return value


    def solve(self,coins,current,amount,dp):

        Inf = float('inf')
        if current == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return Inf
        if dp[current][amount] != -1:
            return dp[current][amount]

        notTaken = self.solve(coins,current - 1, amount,dp)
        taken = Inf

        if amount >= coins[current]:
            taken = 1 + self.solve(coins, current, amount - coins[current],dp)

        
        dp[current][amount] =  min(taken,notTaken)
        return dp[current][amount] 


        
