class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        lar = float("-inf")
        sec_lar = float("-inf")
        
        for i in range(0,len(arr)):
            lar = max(lar,arr[i])
        
        for i in range(0,len(arr)):
            if arr[i] > sec_lar and arr[i] != lar:
                sec_lar = arr[i]
        
        return sec_lar