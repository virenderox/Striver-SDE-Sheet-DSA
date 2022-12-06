class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        return self.optimal(nums)
        
    def optimal(self, arr):
        count1 = 1
        val1 = arr[0]
        
        count2 = 0
        val2 = arr[0]
        
        lenArr = len(arr)
        
        for i in range(1,lenArr):
            
            if arr[i] == val1:
                count1 += 1
                
            elif arr[i] == val2:
                count2 += 1
                
            else:
                if count1 == 0:
                    val1 = arr[i]
                    count1 = 1
                elif count2 == 0:
                    val2 = arr[i]
                    count2 = 1
                    
                else:
                    count1 -=1 
                    count2 -= 1
        ans = []
        
        count = lenArr // 3
        
        c1 = arr.count(val1)
        c2 = arr.count(val2)
        
        if c1 > count :
            ans.append(val1)
        if c2 > count and val1 != val2:
            ans.append(val2)
                
        return ans
        
