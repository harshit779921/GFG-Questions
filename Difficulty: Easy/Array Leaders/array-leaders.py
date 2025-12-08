class Solution:
    def leaders(self, arr):
        result = []
        maxRight = float('-inf')
        
        for x in reversed(arr):
            if x >= maxRight:
                maxRight = x
                result.append(x)
                
        return result[::-1]