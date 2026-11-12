class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count = count + self.checkPalindromes(s, i, i)
            if i + 1 <= len(s)-1:
                count = count + self.checkPalindromes(s, i, i+1)
        return count

        
    def checkPalindromes(self, s, start, end):
        if s[start] == s[end]:
            if start > 0 and end < len(s)-1:
                return 1 + self.checkPalindromes(s, start-1, end+1)
            else:
                return 1
        else: 
            return 0
