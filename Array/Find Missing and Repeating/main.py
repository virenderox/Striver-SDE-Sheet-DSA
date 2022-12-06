#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        
        s = (n * (n + 1)) // 2
        
        p = (n * (n+1) * (2 * n + 1)) // 6
        
        s1 = sum(arr)
        p1 = 0
        
        for val in arr:
            p1 = p1 + (val * val)
            
        #print(s,p,s1,p1)
            
        x_minus_y = s1 - s
        x_plus_y = (p1 - p) // x_minus_y
        
        repeat = (x_plus_y + x_minus_y) // 2
        missing = x_plus_y - repeat
        
        return [repeat,missing]
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
