class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        c = len(cuts)
        cuts.append(n)
        cuts = [0] + cuts
        cuts.sort()
        dp = [[-1 for i in range(c+1)] for j in range(c+1)]
        return self.solve(1,c,cuts,dp)

    def solve(self,i,j,cuts,dp):

        if i > j:
            return 0

        mini = float("inf")

        if dp[i][j] != -1:
            return dp[i][j]

        for ind in range(i,j+1):

            cost = (cuts[j+1] - cuts[i-1]) + self.solve(i,ind-1,cuts,dp) + self.solve(ind +1 , j,cuts,dp)
            mini = min(mini,cost)

        dp[i][j] = mini
        return mini
