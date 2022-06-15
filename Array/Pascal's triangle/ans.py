arr = [[1],[1,1]]
        a = [[1]]
        for val in range(3,numRows+1):
            
            l = self.ArrSum(arr[val - 2], val - 1)
            l.insert(0,1)
            l.append(1)
            arr.append(l)
            
            
        if numRows == 1:
            return a
        else:
            return arr
    
    def ArrSum(self,lst,n):
        
        l = []
        
        for i in range(n-1): 
            l.append(lst[i] + lst[i+1])
            
        return l
