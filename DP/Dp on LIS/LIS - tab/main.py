class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        #intitalization and base case are included in it
        dp = [[0 for i in range(n+2)] for j in range(n+1)]

        #filling up the dp table
        for current in range(n-1,-1,-1):
            for prev in range(current-1,-2,-1):

                taken = float("-inf")
                notTaken = 0 + dp[current+1][prev+1]
                if prev == -1 or nums[current] > nums[prev]:
                    taken = 1 + dp[current+1][current+1]

                dp[current][prev + 1] = max(taken,notTaken)
        
        return dp[0][0]
