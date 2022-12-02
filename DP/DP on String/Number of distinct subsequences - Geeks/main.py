#User function Template for python3

class Solution:
	def distinctSubsequences(self, S):
		
		dp = [1]
		Map = {}
		n = len(S)
		mod = 1000000007
		for val in range(n):
		    
		    dp.append((2 * dp[val]) % mod)
		    
		    if S[val] in Map:
		        
		        ind = Map[S[val]]
		        dp[val+1] = ((dp[val+1]) % mod -  (dp[ind - 1]) % mod) % mod
		        
		       
		    Map[S[val]] = val + 1
		        
		return dp[len(dp) - 1]
		
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends
