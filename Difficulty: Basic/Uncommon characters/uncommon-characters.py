#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        ans = set()
        
        for i in s1:
            if i not in s2:
               ans.add(i)
        
        for j in s2:
            if j not in s1:
                ans.add(j)
                
        res = sorted(ans)
        
        return"".join(res)