class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [-1 for i in range(n+1)]

        return self.solve(arr,0,k,dp)

    def solve(self,arr,ind ,k ,dp):

        if ind == len(arr):
            return 0

        if dp[ind] != -1:
            return dp[ind]

        ln = 0
        maxi = float("-inf")
        ans = float("-inf")

        for j in range(ind,min(ind+k,len(arr))):
            ln += 1
            maxi = max(maxi,arr[j])

            Sum = ln * maxi + self.solve(arr,j+1,k,dp)

            ans = max(ans,Sum)
        dp[ind] = ans
        return ans
