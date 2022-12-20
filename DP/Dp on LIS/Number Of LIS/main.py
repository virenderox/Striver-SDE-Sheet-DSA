class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        count = [1 for i in range(n)]
        Max = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    count[i] = count[j]
                
                elif nums[i] > nums[j] and 1 + dp[j] == dp[i]:
                    count[i] += count[j]



            if dp[i] > Max:
                Max = dp[i]
        print(count,dp)
        nos = 0
        for i in range(n):

            if dp[i] == Max:
                nos += count[i]

        return nos
