#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        # code here
        ans = ''
        for char in range(len(S)):
            if char%2 == 0:
                ans += S[char]
            else:
                continue
        return ans
                