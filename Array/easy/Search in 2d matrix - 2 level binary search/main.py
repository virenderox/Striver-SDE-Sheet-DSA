class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        low = 0
        high = row - 1
        search = []
        #first level binary search
        while low <= high:
        
            mid = (low + high)//2
            if matrix[mid][0] <= target and matrix[mid][col-1] >= target:
                search = matrix[mid]
                break

            elif matrix[mid][0] > target:
                high = mid - 1

            elif matrix[mid][col -1 ] < target:
                low = mid + 1

        
        low = 0
        high = col -1 
        if len(search) == 0:
            return False
        #second level binary search
        while low <= high:
            mid = (low + high) // 2


            if search[mid] == target:
                return True
            elif search[mid] > target:
                high = mid-1
            elif search[mid] < target:
                low = mid + 1


        return False
