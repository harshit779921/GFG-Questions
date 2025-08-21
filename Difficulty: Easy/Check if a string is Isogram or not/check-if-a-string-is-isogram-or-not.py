class Solution:
    def isIsogram(self,s):
        #Your code here
        res = {}
        for char in s:
            if char in res:
                return False
            else:
                res[char] = 1
        return True