class Solution:
	def LongestBitonicSequence(self, nums):
	    n = len(nums)
		dp_inc = self.LIS(nums,n)
		dp_dic = self.LIS(nums[::-1], n)
		#print(dp_inc,dp_dic)
		dp_dic_reverse = dp_dic[::-1]
		#print(dp_inc,dp_dic)
		Max = 0
		for i in range(n):
		    Sum = dp_inc[i] + dp_dic_reverse[i]
		    Max = max(Max,Sum)
		    #print(Sum)

		return Max-1
		        
		      

    def LIS(self,nums,n):
        dp = []
        
        Max = 1
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]


            if dp[i] > Max:
                Max = dp[i]
                
        return dp
               
