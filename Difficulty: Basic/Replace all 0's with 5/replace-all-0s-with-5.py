# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        str_n = str(n)
        res = ""
        for char in str_n:
            if char == '0':
                res = res+'5'
            else:
                res += char
        return(res)