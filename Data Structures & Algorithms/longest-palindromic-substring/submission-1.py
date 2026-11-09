class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 2 choices are add next letter, or finish word

        # can only finish word and replace longest word if its a palindrome

        
        longest_word = s[0]

        for i in range(0, len(s)):
            odd = self.expand(s, i, i)
        
            even = self.expand(s, i, i+1)
    
            if len(odd) > len(longest_word):
                longest_word = odd

            if len(even) > len(longest_word):
                longest_word = even
        
        return longest_word

        
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
            
        return(s[l+1:r])
