class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = 0
        zero = 0

        for i in range(n):

            if nums[i] == 0:
                ind += 1

            else:
                nums[i], nums[zero] = nums[zero], nums[i]
                ind += 1
                zero += 1



        
