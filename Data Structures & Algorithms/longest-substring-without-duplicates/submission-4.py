class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        if len(s) == 0:
            return result
        elif len(s) == 1:
            return 1
        char_set = set(s[0])
        for r in range(1, len(s)):
            
            while l < r and s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            if s[r] not in char_set:
                char_set.add(s[r])
            if r-l+1 > result:
                result = r-l+1
        return result
                
