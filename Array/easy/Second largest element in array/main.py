#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
	    
	    if n < 2:
	        return -1
		maxi = -1
		
		second_maxi = -1
		
		for val in arr:
		    
		    if val > maxi:
		        second_maxi = maxi
		        maxi = val
		        
		    if val > second_maxi and val != maxi:
		        second_maxi = val
		        
		return second_maxi
		
		        
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
