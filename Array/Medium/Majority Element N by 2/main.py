class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        return self.optimal(nums)
        
        
    def brute(self,arr):
        count = 0
        
        dic = {}
        
        for val in nums:
            count += 1
            
            if dic.get(val):
                
                dic[val] += 1
                
            else:
                dic[val] = 1
                
        target = count // 2
        
        for key in dic:
            
            if dic[key] > target:
                return key
            
    def optimal(self, arr):
        count = 1
        val = arr[0]
        lenArr = len(arr)
        
        for i in range(1,lenArr):
            
            if arr[i] == val:
                count += 1
                
            else:
                count -= 1
                
            
            if count == 0:
                val = arr[i]
                count = 1
                
        return val
                
            
        
        
            
        
        
        
        
        
