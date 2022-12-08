class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices,0,True,{})

    def solve(self,prices,ind,buy,dic):

        profit = 0
        #base case 
        if ind == len(prices):
            return 0
            
        currentKey = (ind,buy)
        if currentKey in dic:
            return dic[currentKey]

        #on that particular day if i decide to buy
        if buy :

            profit = max(-prices[ind] + self.solve(prices, ind + 1, False,dic), self.solve(prices , ind + 1, True,dic))

        else:
            profit = max(prices[ind] + self.solve(prices, ind + 1, True,dic), self.solve(prices, ind + 1, False,dic))

        dic[currentKey] = profit
        return profit
        
        
