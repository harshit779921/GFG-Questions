
from typing import List
import copy

class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        temp = copy.deepcopy(arr)
        i = 0
        j = len(arr) - 1
        while i < j:
            temp[i], temp[j] = temp[j], temp[i]
            i += 1
            j -= 1
            
        if temp == arr:
            return True
        else :
            return False
