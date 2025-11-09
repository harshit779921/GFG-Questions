class Solution:   
    def peakElement(self, arr):
        # Code here
        arr.insert(0,float('-inf'))
        arr.append(float('-inf'))
        
        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
                
            else:
                continue
        return 0