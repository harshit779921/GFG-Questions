#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        # Brute Force
        # lst = []
        
        # for i in range(0, len(arr)-1):
        #     for j in range(i+1, len(arr)):
        #         if arr[i] + arr[j] == 0:
        #             if arr[i] > arr[j]:
        #                 output = arr[j], arr[i]
                        
        #             else:
        #                 output = arr[i], arr[j]
                        
        #             lst.append(output)
                
        #         else: 
        #             continue
        
        # ans = list(set(lst))
        
        # ans.sort()
        
        # return ans
        
        # Optimal Solution
        arr.sort()
        i=0
        j=len(arr)-1
        
        e_set=set()
        lst=[]
        while i < j :
            if arr[i]+arr[j]==0:
                i+=1
                j-=1
                if (arr[i-1],arr[j+1]) in e_set:
                    continue
                else:
                    e_set.add((arr[i-1],arr[j+1]))
                    
                    lst.append([arr[i-1],arr[j+1]])
            elif arr[i]+arr[j]>0:
                j-=1
            else:
                i+=1
                
        return lst