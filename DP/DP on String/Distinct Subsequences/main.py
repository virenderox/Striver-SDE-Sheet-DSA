class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def dfs(i,j):
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0


            currentKey = (i,j)
            if currentKey in cache:
                return cache[currentKey]

            if s[i] == t[j]:
                cache[currentKey] = dfs(i+1,j+1) + dfs(i+1,j)

            else:
                cache[currentKey]  = dfs(i+1,j)

            return cache[currentKey]

        return dfs(0,0)
