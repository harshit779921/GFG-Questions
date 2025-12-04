class Solution:
    def merge(self, S1, S2):
        result = ""
        
        if(len(S1) <= len(S2)):
            for i in range(len(S1)):
                result += (S1[i] + S2[i])
            
            result += S2[len(S1):]
        else:
            for i in range(len(S2)):
                result += (S1[i] + S2[i])
            
            result += S1[len(S2):]
        
        return result