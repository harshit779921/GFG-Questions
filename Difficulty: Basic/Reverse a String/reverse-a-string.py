#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        res = ''
        for i in range(len(s)-1,-1,-1):
            res = res+ s[i]
        return res
        
        # Using Slicing
        # return s[::-1]