class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        total_list = a + b
        union = 0
        dic = {}
        for val in total_list :
            
            if val not in dic:
                dic[val] = True
                union += 1
                
        return union
                
