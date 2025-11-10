#User function Template for python3

class Solution:
    def convert(self, s):
        # code here
        new_s = s.split(" ")
        
        for i in range(len(new_s)):
            word = new_s[i]
            word_upper = word[0].upper()
            new_word = word_upper + word[1:]
            new_s[i] = new_word
            
        final_s = " ".join(new_s)
        return final_s