len_s = len(s)
        len_p = len(p)

        #intialize the DP
        dp = [[False for i in range(len_s + 1)] for j in range(len_p + 1)]

        # as s = "" and p = "" ---> always True
        dp[len_p][len_s] = True


        #  intialization of last coloum if p[i] == "*" then take down one
        for i in range(len_p-1,-1,-1):
            if p[i] == "*":
                dp[i][len_s] = dp[i+1][len_s]

        #filling up the Dp table
        for i in range(len_p - 1, -1, -1):
            for j in range(len_s -1 , -1 , -1):

                # p[i] is ? the always take digonal value
                if p[i] == '?':
                    dp[i][j] = dp[i+1][j+1]

                #p[i] is * take value of down or right 
                elif p[i] == '*':
                    dp[i][j] = dp[i+1][j] or dp[i][j+1]
                
                #P[i] is charcheter we have two choices again
                else:

                    #if character matches with pattern char the take diogonal value
                    if s[j] == p[i]:
                        dp[i][j] = dp[i+1][j+1]
                        
                    #else if not matches return False
                    else:
                        dp[i][j] = False

        return dp[0][0]
