class Solution:
    def getAlternates(self, arr):
        # Code Here
        output = []
        for i in range(len(arr)):
            if i%2==0:
                output.append(arr[i])
            else:
                continue
        return (output)