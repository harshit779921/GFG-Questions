#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		op = S[0]
		
		for i in range(len(S)-1):
		    if S[i] == " ":
		        op += S[i+1]
		return op