class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        k = n - 2
        while k >= 0:
            if nums[k] < nums[k + 1]:
                break
            k -= 1
       # print(k)
            
        if k < 0:
            #print("in IF")
            nums.sort()
            return nums
        
        else:
           # print("HI")
            l = n - 1
            while l > k:
                if nums[l] > nums[k]:
                    break
                l = l - 1
                
            #print(k,l)
                    
            nums[k] , nums[l] = nums[l] , nums[k]
            nums[k+1:] = sorted(nums[k+1:])
            
            return nums
