class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[-1 for i in range(n+1)] for j in range(n)]

        return self.solve(nums,0,-1,n, dp)

    def solve(self,nums,current,prev,n,dp):

        #base case 
        if current == n:
            return 0

        if dp[current][prev + 1] != -1:
            return dp[current][prev + 1]

        #recusive relation
        taken = float("-inf")
        notTaken = 0 + self.solve(nums,current + 1, prev,n,dp)
        if prev == -1 or nums[current] > nums[prev]:
            taken = 1 + self.solve(nums,current+1,current,n,dp)

        dp[current][prev + 1] = max(taken,notTaken)

        return dp[current][prev + 1]



        


        
