#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        upper=0
        lower=0
        number=0
        special=0
        for ch in s.strip():
            if ch.isupper():
                upper += 1
            elif ch.islower():
                lower +=1
            elif ch.isnumeric():
                number +=1
            elif not ch.isspace():
                special +=1
                
        return upper, lower, number, special
                