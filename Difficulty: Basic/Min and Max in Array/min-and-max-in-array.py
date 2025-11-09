class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
            elif arr[i] > max:
                max = arr[i]
        return min, max
         