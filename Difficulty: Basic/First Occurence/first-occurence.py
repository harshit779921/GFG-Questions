class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        len_pat = len(pat)

        for i in range(len(txt) - len_pat + 1):
          if txt[i:i+len_pat] == pat:
             return i
                
        return -1 