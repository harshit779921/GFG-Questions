#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        res = ""
        
        for i in str1:
            if(i in str2):
                continue
            else:
                res += i
        
        return res