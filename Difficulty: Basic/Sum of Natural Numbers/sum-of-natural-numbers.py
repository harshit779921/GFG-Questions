class Solution:
    def findSum(self, n):
        # code here
        res = 0
        for i in range(n+1):
            if i == 0:
                continue
            else:
                res = res+i
        return res
        
