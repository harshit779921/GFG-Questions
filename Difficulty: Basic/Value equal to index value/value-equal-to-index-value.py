#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        lst = []
        
        for i in range(len(arr)):
            if i+1 == arr[i]:
                lst.append(arr[i])
                
        return lst