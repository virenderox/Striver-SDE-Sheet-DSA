#User function Template for python3

   
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        
        return self.solve(0,0,a,b,{})
            
    def solve(self,current_i, current_j,a,b,dic):
        
        
        if current_i == a-1 and current_j == b-1:
            #print("I")
            return 1
        
        if current_i == a or current_j  == b:
            return 0
            
        currentKey = (current_i,current_j)
        if currentKey in dic:
            return dic[currentKey]
            
        down = self.solve(current_i + 1, current_j,a,b,dic)
        right = self.solve(current_i,current_j + 1 ,a ,b,dic)
        
        dic[currentKey] =  down + right
        return dic[currentKey]
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends
