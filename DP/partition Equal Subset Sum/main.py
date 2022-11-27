# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        
        Sum = sum(arr)
        if Sum % 2 != 0:
            return 0
            
            
        target = Sum // 2
        dp = [[-1 for i in range(target+1)] for j in range(N+1)]
        return self.solve(arr,N-1,target,dp)
            
    def solve(self,arr,current_i,target,dp):
        
        
        if target == 0:
            return True
            
        if current_i == 0:
            return arr[0] == target
        
        if dp[current_i][target] != -1:
            return dp[current_i][target]
        
        notTaken = self.solve(arr,current_i - 1,target,dp)
        taken = False   
        if arr[current_i] <= target:
            taken = self.solve(arr,current_i - 1,target - arr[current_i],dp)
            
        dp[current_i][target] = taken or notTaken    
            
        return dp[current_i][target]
            
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
