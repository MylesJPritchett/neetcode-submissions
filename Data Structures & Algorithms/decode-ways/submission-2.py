class Solution:
    def numDecodings(self, s: str) -> int:

        

        prev1, prev2 = 1, 1
        
        for i in range(1, len(s)+1):
            cur = 0
            if int(s[i-1]) > 0:
                cur += prev1

            
            if i >=2 and 10 <= int(s[i-2:i]) <= 26:
                cur += prev2

            prev2 = prev1
            prev1 = cur
            
        return prev1