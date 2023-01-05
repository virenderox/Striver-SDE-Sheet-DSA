class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = []
        ln = len(nums)
        
        # two sum
        start = 0
        end = ln - 1
        arr = nums[:]
        nums.sort()
        while start < end:

            Sum = nums[start] + nums[end]
            
            if Sum == target:
                n1 = nums[start]
                n2 = nums[end]
                break

            elif Sum > target:
                end -= 1

            else:
                start += 1
        for i in range(ln):
            if arr[i] == n1:
                ans.append(i)
                arr[i] = 1000000000
            if arr[i] == n2:
                ans.append(i)
        return ans
