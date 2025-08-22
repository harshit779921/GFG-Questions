
class Solution:
    def swapKth(self, arr, k):
        # Code Here
        n = len(arr)
        arr[k-1], arr[n-k] = arr[n-k],arr[k-1]
        
        return arr
        
