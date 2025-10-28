class Solution:
    def getAlternates(self, arr):
        # Code Here
        Output = []
        for i in range(len(arr)):
            if i%2==0:
                Output.append(arr[i])
            else:
                continue
        return Output