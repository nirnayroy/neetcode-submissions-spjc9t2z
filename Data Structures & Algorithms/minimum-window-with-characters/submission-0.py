class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        min_len = float('inf')
        window = {}
        string_t = {}
        string_s = {}
        for char in t:
            if char in string_t:
                string_t[char] += 1
            else:
                string_t[char] = 1
                window[char] = 0
        
        for char in s:
            if char in string_s:
                string_s[char] += 1
            else:
                string_s[char] = 1

        for char in string_t.keys():
            if char not in string_s or string_s[char] < string_t[char]:
                return ''

        have = 0
        need = len(string_t.keys())
        for r in range(0, len(s)):
            print(window)
            print(have)
            print(l)
            print(r)
            if s[r] in window:
                window[s[r]] += 1
                if window[s[r]] == string_t[s[r]]:
                    have += 1
            while need == have:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    ans = s[l:r+1]
                
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < string_t[s[l]]:
                        have -= 1
                l+=1
        return ans
        
        
        

        

            
            
