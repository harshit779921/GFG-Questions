class Solution:
    def findTwoElement(self, arr):
        dic = {}
        ans = []

        # Count frequency
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        repeating = None
        missing = None

        # Find repeating
        for key, value in dic.items():
            if value > 1:
                repeating = key
                break

        # Find missing
        n = len(arr)
        for num in range(1, n+1):
            if num not in dic:
                missing = num
                break

        return [repeating, missing]
