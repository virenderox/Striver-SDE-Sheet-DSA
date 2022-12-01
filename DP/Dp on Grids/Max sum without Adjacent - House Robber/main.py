#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		return self.solve(arr,n,n-1,{})
		
	def solve(self,arr,n,current,dic):
	    
	    mod = 1000000007
	    
	    if current < 0:
	        return 0
	        
	    if current == 0:
	        return arr[current]
	        
	    if current in dic:
	        return dic[current]
	        
	    take = ((self.solve(arr,n,current - 2,dic) % mod) + (arr[current] % mod)) % mod
	    notTake = self.solve(arr,n,current - 1,dic) % mod
	    
	    dic[current] = max(take, notTake)
	    return dic[current]


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
