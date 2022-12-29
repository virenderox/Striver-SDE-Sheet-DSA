class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        nums.reverse()

        front_i = 0
        front_j = k-1

        while front_i < front_j:
            nums[front_i],nums[front_j] = nums[front_j],nums[front_i]
            front_i += 1
            front_j -= 1

        back_i = k
        back_j = n-1

        while back_i < back_j:
            nums[back_i], nums[back_j] = nums[back_j], nums[back_i]
            back_i += 1
            back_j -= 1
