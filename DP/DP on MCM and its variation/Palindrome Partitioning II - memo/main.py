class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        dp = [-1 for i in range(n + 1)]
        return self.solve(s,0,n,dp) - 1

    def solve(self,s,i,n,dp):

        if i == n: 
            return 0

        if dp[i] != -1:
            return dp[i]

        min_cost = float("inf")
        for k in range(i,n):

            if self.isPalindrome(s,i,k):
                cost = 1 + self.solve(s,k+1,n,dp)
                if cost < min_cost:
                    min_cost = cost
        dp[i] = min_cost
        return min_cost

            
    def isPalindrome(self,s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True

