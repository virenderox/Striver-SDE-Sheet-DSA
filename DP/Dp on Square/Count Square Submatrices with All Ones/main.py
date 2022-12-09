class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for i in range(col)] for j in range(row)]
        total_sum = 0
        for r in range(row):

            for c in range(col):

                if r == 0 or c == 0:
                    dp[r][c] = matrix[r][c]

                else:
                    if matrix[r][c] == 1:
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

            total_sum += sum(dp[r])

        #print(dp)

        return total_sum

            




