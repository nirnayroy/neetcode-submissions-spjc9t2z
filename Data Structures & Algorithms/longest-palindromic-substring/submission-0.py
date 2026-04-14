class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result_len = 0
        result = ""

        for i in range(len(s)):
            # odd
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                res = s[l:r+1]
                len_res = r-l+1
                l -= 1
                r += 1
                if len_res>result_len:
                    result = res
                    result_len = len_res

            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                res = s[l:r+1]
                len_res = r-l+1
                l -= 1
                r += 1
                if len_res>result_len:
                    result = res
                    result_len = len_res
            
            
        return result
