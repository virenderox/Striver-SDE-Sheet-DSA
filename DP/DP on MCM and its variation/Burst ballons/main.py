class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        l_n = len(nums)
        dp = [[-1 for i in range(l_n + 1)] for j in range(l_n + 1)]
   

        def dfs(l,r):
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            dp[l][r] = 0
            for i in range(l,r+1):
                coins = nums[l-1] * nums[i] * nums[r + 1]
                coins += dfs(l, i-1) + dfs(i + 1, r)
                dp[l][r] = max(dp[l][r], coins)
            return dp[l][r]

        return dfs(1,len(nums) - 2)
