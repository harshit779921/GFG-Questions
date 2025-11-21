class Solution:
	def swapElements(self, arr):
	    #Code here
	    
	    for i in range(2,len(arr)):
	        arr[i], arr[i-2] = arr[i-2], arr[i]