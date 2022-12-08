from typing import List


class Solution:
    def maxProfit(self, n : int, prices : List[int]) -> int:
        dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(len(prices) + 1)]
        return self.tab(prices,n,dp)
        #return self.solve(prices, 0 , True, 2,dp)
        
    def tab(self,prices,n, dp):
        
        for current in range(n-1,-1,-1):
            for buy in range(2):
                for transaction in range(1,3):
                    if buy :

                        dp[current][buy][transaction] =  max(-prices[current] + dp[current + 1][False][transaction], dp[current + 1][ True][ transaction])

                    else:
                        dp[current][buy][transaction] =  max(prices[current] + dp[current + 1][True][transaction-1], dp[current + 1][False][ transaction])

        return dp[0][1][2]
                    
            

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


        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends
