class Solution:
    def findDuplicates(self, arr):
        # code here
        freq = {}
        ans = []
        
        for i in arr:
            if i in freq:
                freq[i] += 1
                
            else:
                freq[i] = 1
                
        for key, value in freq.items():
            if value > 1:
                ans.append(key)
                
        return ans