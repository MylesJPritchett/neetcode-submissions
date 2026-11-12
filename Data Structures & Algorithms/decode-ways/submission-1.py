class Solution:
    def numDecodings(self, s: str) -> int:

        

        prev1, prev2 = 1, 1
        
        for i in range(1, len(s)+1):
            cur = 0
            if int(s[i-1]) > 0:
                cur += prev1

            twoDigit = int(s[i-2]+s[i-1])
            if i >=2 and twoDigit >= 10 and twoDigit <= 26:
                cur += prev2
                
            prev2 = prev1
            prev1 = cur
            
        return cur