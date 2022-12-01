#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
       #dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        return self.Lcs(s1,s2,x,y,{})
        #return self.Lcs(text1,text2,n ,m ,{})

    def LcsTable(self,s1,s2,n,m,dp):

        for i in range(1,n+1):
            for j in range(1,m+1):

                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])



    def Lcs(self,s1,s2,n,m,mat):

        if n == 0 or m == 0:
            return 0

        currentKey  = (n,m)

        if currentKey in mat:
            return mat[currentKey]


        if s1[n-1] == s2[m-1]:
            mat[currentKey] = 1 + self.Lcs(s1,s2,n-1,m-1,mat)
            return mat[currentKey]

        else:
            mat[currentKey] = max(self.Lcs(s1,s2,n-1,m,mat), self.Lcs(s1,s2,n,m-1,mat))

            return mat[currentKey]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
