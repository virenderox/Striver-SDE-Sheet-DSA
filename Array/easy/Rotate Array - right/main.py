#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,nums,k,n):
       
        if k > n:
            k = k % n
        nums.reverse()

        front_i = 0
        front_j = n-k-1

        while front_i < front_j:
            nums[front_i],nums[front_j] = nums[front_j],nums[front_i]
            front_i += 1
            front_j -= 1

        back_i = n-k
        back_j = n-1

        while back_i < back_j:
            nums[back_i], nums[back_j] = nums[back_j], nums[back_i]
            back_i += 1
            back_j -= 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
