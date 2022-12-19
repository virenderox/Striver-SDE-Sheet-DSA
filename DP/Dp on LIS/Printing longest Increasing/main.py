class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        n = len(nums)
        dp = [1 for i in range(n)]
        dp[0] = 1
        cache = []
        Max = 1
        last = -1
        ans = []

        nums.sort()
        
        for i in range(n):
            cache.append(i)
            for j in range(i):
                if nums[i] > nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    cache[i] = j
       
            if dp[i] > Max:
                Max = dp[i]
                last = i

        ans.append(nums[last])
        while cache[last] != last and last != -1:

            last = cache[last]
            ans.append(nums[last])
        
       

        return ans

