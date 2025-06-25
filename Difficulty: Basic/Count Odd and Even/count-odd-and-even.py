class Solution:
	def countOddEven(self, arr):
		#Code here
		even = 0
		odd = 0
		for i in arr:
		    if i%2==0:
		        even = even+1
		    else :
		        odd = odd+1
		return (odd,even)