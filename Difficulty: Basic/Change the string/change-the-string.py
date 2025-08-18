#User function Template for python3


class Solution:
    def modify(self, s):
        # code here
        for i in range(len(s)):
            if s[0].isupper():
                s = s.upper()
            else:
                s= s.lower()
        return s