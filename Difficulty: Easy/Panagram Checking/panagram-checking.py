class Solution:
    def checkPangram(self,s):
        #code here
        x=[]
        for i in s.lower():
            if i.isalpha():
                x.append(i)
        if len(set(x))==26:
            return True
        return False