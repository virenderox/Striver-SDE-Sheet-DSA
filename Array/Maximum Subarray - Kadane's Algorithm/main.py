def maxSubArray(self, nums: List[int]) -> int:

        Max = nums[0]
        Sum = nums[0]

        for val in nums[1:]:

            Sum += val
            if Sum < val:
                Sum = val

            Max = max(Max,Sum)

        return Max
        
