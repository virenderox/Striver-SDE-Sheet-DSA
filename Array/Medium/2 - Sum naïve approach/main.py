class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = self.optimal(nums,target)
        return ans
        
        
        
    def optimal(self,nums,target):
        
        n = len(nums)
        ans = []
        for ind in range(n-1):
            
            temp_set = set(nums[ind + 1 : ])
            if (target -  nums[ind]) in temp_set:
                val = nums[ind]
                nums[ind] = 100000000000000
                ans.append(ind)
                ans.append(nums.index(target - val))
                break
                
        return ans
                
                
