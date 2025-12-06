class Solution:
    def areRotations(self, s1, s2):
        # code here
        if(len(s1)!=len(s2)):
            return False
        str=s1+s1
        return True if s2 in str else False