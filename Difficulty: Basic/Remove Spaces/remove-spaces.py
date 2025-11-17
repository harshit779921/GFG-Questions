#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        new_var = ''
        
        for i in s:
            if i == " ":
                continue
            else:
                new_var += i
                
        return new_var