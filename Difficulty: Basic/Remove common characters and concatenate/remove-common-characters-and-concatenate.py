class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        word = ''
        
        for i in s1:
            if i not in s2:
                word += i
                
        for j in s2:
            if j not in s1:
                word += j
                
        if len(word)>=1:
            return word
            
        return -1