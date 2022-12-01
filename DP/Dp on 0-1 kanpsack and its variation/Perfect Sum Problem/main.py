#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		
		dp = [[-1 for _ in range(sum + 1)] for _ in range(n+1)]
		return self.solve(arr,n-1,sum,dp)
		
	def solve(self,arr,current,target,dp):
	    
	    mod = 1000000007
	    if current == 0:
	        if target == 0 and arr[0] == 0:
	            return 2
	        if target == 0 or target == arr[0]:
	            return 1
	        return 0
	    
	    if dp[current][target] != -1:
	        return dp[current][target]
	        
	       
	    notTaken = self.solve(arr,current -1 , target,dp)
	    taken = 0
	   
	    if target >= arr[current]:
	       
	        taken = self.solve(arr,current - 1, target - arr[current],dp)
	       
        dp[current][target] = ((taken % mod) + (notTaken % mod)) % mod
	    return dp[current][target]
	       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
