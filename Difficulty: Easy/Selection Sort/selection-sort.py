class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            min_idk = i
            for j in range(i+1,n):
                if arr[j] < arr[min_idk]:
                    min_idk = j
            arr[i],arr[min_idk] = arr[min_idk],arr[i]
        return arr