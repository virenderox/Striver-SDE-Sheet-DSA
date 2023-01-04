class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #using hasp map - but using extra space

        memo = {}

        for val in nums:

            if val in memo:
                memo[val] += 1

            else:
                memo[val] = 1

        for key in memo:

            if memo[key] == 1:
                return key
