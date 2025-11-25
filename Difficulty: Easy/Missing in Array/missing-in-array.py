class Solution:
    def missingNum(self, arr):
        # code here
        # Brute
        # for i in range(len(arr)+1):
        #     if i+1 in arr:
        #         continue
        #     else:
        #         return i+1
        
        # Optimal
        sum = 0
        
        for i in range(len(arr)):
            sum = sum + arr[i]
        n = len(arr) + 1
        exact_sum = (n*(n+1))//2
        
        res = exact_sum - sum
        
        return res