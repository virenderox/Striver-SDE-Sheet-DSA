class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        dup = 1
        n = len(nums)
        ind = 0
        swap = 1
        for i in range(n-1):

            if nums[ind] == nums[ind + 1]:
                ind += 1

            else:
                swap += 1
                nums[dup] = nums[ind+1]
                ind += 1
                dup += 1

        return swap
