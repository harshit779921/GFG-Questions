class Solution:
    def encode(self, s : str) -> str:
        # code here
        curr_str = s[0]
        count = 1
        res = ''
        for i in range(1,len(s)):
            if s[i] == curr_str:
                count += 1
            else:
                res += f'{curr_str}{count}'
                curr_str = s[i]
                count = 1
        res += f'{curr_str}{count}'
        return res