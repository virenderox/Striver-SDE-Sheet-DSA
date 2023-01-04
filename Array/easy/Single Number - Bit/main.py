class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #using hasp map - but using extra space
        #return self.solveHash(nums)

        #using bit 
        return self.solveBit(nums)

    def solveBit(self,nums):

        xor = 0
        for val in nums:
            xor ^= val

        return xor
