#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        # ans = 0
        # x = n
        # count = 0
        # while x>0:
        #     count +=1
        #     x= x//10
        
        # x = n
        
        # while x>0:
        #     last_digit = n%10
        #     ans = ans + (x**count)
        #     x = x//10
        
        # return n == ans
        
        # Using For Loop
        temp  = n
        count = len(str(n))
        ans = 0
        
        for i in range(count):
            last_digit = temp%10
            ans = ans + (last_digit**count)
            temp = temp//10
            
        return n == ans