class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for i in range(1, len(s)+1):
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]

            twoDigit = int(s[i-2]+s[i-1])
            if i >=2 and twoDigit >= 10 and twoDigit <= 26:
                dp[i] += dp[i-2]

            print(dp)
        return dp[len(s)]