class Solution:
    def isPalindrome(self, n):
		# code here
		ans = 0
		temp = n
		while n>0:
		    last_digit = n%10
		    ans = (ans*10) + last_digit
		    n = n//10
        return temp == ans