class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key = len)
       # print(words)
        n = len(words)
        dp = [1 for i in range(n)]
        dp[0] = 1
        Max = 1
        
        for i in range(n):
            for j in range(i):
                bol = self.compare(words[i], words[j])
                if  bol and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
            if dp[i] > Max:
                Max = dp[i]

        return Max

    def compare(self,s1,s2):

       # print(s1,s2)

        if len(s1)  != len(s2) + 1:
            return False

        first = 0
        second = 0

        while first < len(s1):

            if second < len(s2) and s1[first] == s2[second] :
                first += 1
                second += 1

            else:
                first += 1

        if first == len(s1) and second == len(s2):
            return True

        return False
