class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        common = []
        dic = {}
        for val in nums1:

            if val in nums2:
                if val not in dic:
                    common.append(val)
                    dic[val] = True

        return common

            
                
