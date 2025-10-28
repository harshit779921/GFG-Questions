class Solution:
	def countOddEven(self, arr):
		#Code here
		even_num = 0
		odd_num = 0
		for num in arr:
		    if num%2 == 0:
		        even_num += 1
		    else:
		        odd_num += 1
		return (odd_num, even_num)