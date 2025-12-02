class Solution:
    def areAnagrams(self, s1, s2):
        dict1 = {}
        dict2 = {}
        
        if len(s1) != len(s2):
            return False

        for i in s1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for j in s2:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1

        for k in dict1.keys():
            if dict1[k] != dict2.get(k, 0):   # use get() to avoid key error
                return False

        return True
