#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		vowel = ['a', 'i', 'e', 'o', 'u']
		new_var = ''
		for i in s:
		    if i in vowel:
		        continue
		    else:
		        new_var += i
		        
		return new_var
		        