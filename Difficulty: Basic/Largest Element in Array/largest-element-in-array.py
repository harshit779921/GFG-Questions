class Solution:
    def largest(self, arr):
        # code here
        ans = 0
        for i in range(len(arr)):
            if arr[i]> ans:
                ans = arr[i]
            else:
                continue
            
        return (ans)
        
