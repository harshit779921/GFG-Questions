class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        dic = {}
        
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else : 
                dic[arr[i]] = 1
                
        for key, value in dic.items():
            if value%2 != 0:
                return key
                