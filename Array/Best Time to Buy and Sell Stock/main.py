class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        maxProfit = 0
        Min = 10000
        
        lenPrice = len(prices)
        
        for ind in range(lenPrice):
            
            if Min > prices[ind]:
                Min = prices[ind]
                
            profit = prices[ind] - Min
            
            if profit > maxProfit:
                maxProfit = profit
                
        
        return maxProfit
            
