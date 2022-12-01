#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        return self.solve(0,n,{})
        
    def solve(self,current,n,dic):
        
        if current == n:
            return 1
        mod = 1000000007
            
        if current > n:
            return 0
        
        if current in dic:
            return dic[current]
            
        one = self.solve(current + 1, n,dic)
        second = self.solve(current + 2, n,dic)
        
        dic[current] = ((one % mod) + (second % mod) ) % mod
        return dic[current]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends
