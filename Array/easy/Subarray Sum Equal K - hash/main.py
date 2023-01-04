class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        # we are using prefix-Sum
        prefix = ans = 0

        memo = {}
        memo[prefix] = 1

        for val in nums:

            prefix += val
            current = prefix - k

            if current in memo:
                ans += memo[current]

            if prefix in memo:
                memo[prefix] += 1

            else:
                memo[prefix] = 1

        return ans
