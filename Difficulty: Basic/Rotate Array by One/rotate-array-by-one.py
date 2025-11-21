#User function Template for python3

class Solution:
    def rotate(self, arr):
        # Using Slicing
        # arr[:] = arr[n-1:] + arr[0:n-1]
        # return arrn = len(arr)
        
        # Without Slicing
        
        temp = arr[len(arr)-1]
        
        for i in range(len(arr)-2,-1,-1):
            arr[i+1] = arr[i]
        arr[0] = temp