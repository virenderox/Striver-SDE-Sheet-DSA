#User function Template for python3

class Solution:
    def maximumProfit(self, prices, n):
        
        total_profit = 0
        buy = 0
        sell = 0
        
        for i in range(1,n):
            
            if prices[i] >= prices[i-1]:
                sell += 1
            else:
             
                total_profit += (prices[sell] - prices[buy])
                buy = i
                sell = i
                
        
        total_profit += (prices[sell] - prices[buy])
                
        return total_profit
        #Code here


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
