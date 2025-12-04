#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        char = ""
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                continue
            else:
                char += s[i]
                
        char = char + s[-1]
        
        return char