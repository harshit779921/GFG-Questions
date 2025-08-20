#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        count_camel = 0
        for ch in s.strip():
            if ch.isupper():
                count_camel += 1
        return count_camel