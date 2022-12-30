class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0
        count = 0
        maxi = -1
        while i < n:

            if nums[i] == 1:
                count += 1

            elif nums[i] == 0:
                count = 0

            i += 1
           # print(count)
            if count > maxi:
                maxi = count

        return maxi
